#!/usr/bin/env python
from pwn import *
import pickle
import os
import angr
from strategies import *
import argparse

libc_path = "./bins/libc.so.6"
libc_symbol_path = "./bins/389d485a9793dbe873f0ea2c93e02efaa9aa3d.debug"
libc = ELF(libc_path, checksec=False)

proj = angr.Project(libc_path, main_opts={"base_addr": 0})

def get_symbols():
    symbols = [(x, y, libc.functions[x].size) for x, y in libc.symbols.items() if x in libc.functions]

    output = subprocess.run(f"readelf -W -s {libc_symbol_path}".split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode()
    for line in output.splitlines():
        elems = line.split()
        if len(elems) != 8 or elems[0] == "Num:":
            continue
        _, addr_str, size_str, _, _, _, _, sym_name = elems
        addr = int(addr_str, 16)
        size = int(size_str)
        if addr == 0:
            continue
        if '@' in sym_name:
            sym_name = sym_name.split('@')[0]
        symbols.append((sym_name, addr, size))
    return symbols

libc_symbols = get_symbols()

def get_symbol_from_addr(target_addr):
    for sym_name, addr, _ in libc_symbols:
        if addr == target_addr:
            return sym_name

def print_path(state):
    main_addr = list(state.history.bbl_addrs)[0]
    main_symbol = get_symbol_from_addr(main_addr)
    backtrace = [(main_addr, main_symbol)]
    for i, (addr, jump_method) in enumerate(zip(state.history.bbl_addrs, list(state.history.jumpkinds)[:-1])):
        print(f"### Frame {i}: ", end="")
        offset = 0
        if jump_method == "Ijk_Call":
            func_name = get_symbol_from_addr(addr)
            if func_name is None:
                backtrace.append((addr, "unknown"))
            else:
                backtrace.append((addr, func_name))
        elif jump_method == "Ijk_Ret":
            backtrace.pop()
            offset = addr - backtrace[-1][0]
        elif jump_method == "Ijk_Boring":
            offset = addr - backtrace[-1][0]
        else:
            print("???")
        if offset != 0:
            print(f"`{backtrace[-1][1]}+{offset}`")
        else:
            print(f"`{backtrace[-1][1]}`")
        
        block = proj.factory.block(addr)
        print("~~~asm")
        block.pp()
        print("~~~")

    print("-"*20)
    print("Call stack:")
    for i, (_, name) in enumerate(backtrace):
        print("  "*i + f"- `{name}`")
        if i == len(backtrace) - 1:
            print("  "*(i+1) + f'- `{repr(state.regs.rip).removeprefix("<BV64 ").removesuffix(">")}`')

    print("-"*20)
    print("Conditions:")
    print("~~~cpp")
    for jump_guard in state.history.jump_guards:
        if not jump_guard.is_true():
            print(repr(jump_guard).removeprefix("<Bool ").removesuffix(">"))
    print("~~~")
    
    print("-"*20)
    print("Register values at the call:")
    # reg_list = [x for x in state.arch.default_symbolic_registers if x not in ['rip', 'rsp']]
    for reg in state.arch.default_symbolic_registers:
        print(f"- `{reg}`: " + repr(getattr(state.regs, reg)).removeprefix("<BV64 ").removesuffix(">"))
    
    print("-"*30)


def examine_file(filename, mode):
    try:
        with open(f"./{filename}", 'rb') as f:
            states = pickle.load(f)
        if mode == "all":
            print(f"{len(states)} states")
            for i, state in enumerate(states):
                print(f"## State {i}")
                print_path(state)
        elif mode == "first":
            print_path(states[0])
        elif mode == "shortest":
            # Goes through the least amount of jumps
            criteria = list(map(lambda s: len(s.history.bbl_addrs), states))
            state_index = criteria.index(min(criteria))
            print(f"State {state_index} is the shortest of {len(states)} states")
            print_path(states[state_index])
        elif mode == "best":
            # Shortest path for each ending address
            criteria = list(map(lambda s: len(s.history.bbl_addrs), states))
            print(f"{len(states)} states with {criteria} frames")
            found_exits = []
            for i, state in enumerate(states):
                block = proj.factory.block(state.history.bbl_addrs[-1])
                last_addr = block.instruction_addrs[-1]
                if last_addr in found_exits:
                    continue
                print(f"## State {i} with ending {hex(last_addr)}")
                print_path(state)
                found_exits.append(last_addr)
    except ValueError as e:
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="If file is a directory, examine all files in it")
    parser.add_argument("--mode", choices=("all", "first", "shortest", "best"), default="all")
    args = parser.parse_args()
    if os.path.isdir(args.file):
        os.chdir(args.file)
        paths = os.listdir()
        for path in paths:
            print(f"# {os.path.basename(path)}")
            examine_file(path, args.mode)
            break
    else:
        print(f"# {os.path.basename(args.file)}")
        examine_file(args.file, args.mode)
