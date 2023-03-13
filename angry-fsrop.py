from pwn import *
context.arch = 'amd64'

######## CONFIGURATION ##########
TIMEOUT = 60
MAX_STEP = 100
libc_path = "./bins/libc.so.6"
libc_symbol_path = "./bins/389d485a9793dbe873f0ea2c93e02efaa9aa3d.debug"
output_dir = "outputs"
#################################

libc = ELF(libc_path)
raw_vtable_bytes = libc.section('__libc_IO_vtables')
os.makedirs(output_dir, exist_ok=True)

def get_symbols():
    symbols = [(x, y, libc.functions[x].size) for x, y in libc.symbols.items() if x in libc.functions]

    output = subprocess.getoutput(f"readelf -W -s {libc_symbol_path}")
    for line in output.splitlines():
        elems = line.split()
        if len(elems) != 8:
            continue
        _, addr_str, size_str, _, _, _, _, sym_name = elems
        try:
            addr = int(addr_str, 16)
        except Exception:
            continue
        size = int(size_str)
        if addr == 0:
            continue
        if '@' in sym_name:
            sym_name = sym_name.split('@')[0]
        symbols.append((sym_name, addr, size))
    return symbols

symbols = get_symbols()

# Get all the pointers in the vtable section
ptrs = []
for i in range(0, len(raw_vtable_bytes), 8):
    ptr = u64(raw_vtable_bytes[i:i+8])
    if ptr == 0:
        continue
    ptrs.append(ptr)

# Get names of all the functions that need to be examined
func_names = []
for ptr in ptrs:
    for name, start_addr, _ in symbols:
        if start_addr == ptr:
            func_names.append(name)
            break
    else:
        print(ptr)
        print(func_names)
        raise
func_names = set(func_names)

# Print disassembly
# for func_name in func_names:
#    for name, addr, size in symbols:
#        if func_name != name:
#            continue
#        disassembly = e.disasm(addr, size)
#        print(name, hex(addr))
#        print(disassembly)
#        print("="*0x10)

import angr
import claripy
import archinfo
import logging
from strategies import *

logging.getLogger("angr.storage.memory_mixins.default_filler_mixin").setLevel("ERROR")
logging.getLogger("angr.engines.successors").setLevel("ERROR")

target_symbols = {(x, y, z) for x, y, z in symbols if x in func_names}

FP_ADDR = 0x4000000
FILE_STRUCT_ADDR = 0x5000000
WIDE_DATA_ADDR = 0x6000000
CODECVT_ADDR = 0x7000000
proj = angr.Project(libc_path, main_opts={"base_addr": 0})

class StructElement():
    def __init__(self, name: str, size: int, offset: int, prefix: str=""):
        self.name = name
        self.size = size
        self.offset = offset
        self.prefix = prefix
        self.BVS = claripy.BVS(f"{self.prefix}{self.name}", self.size, explicit_name=True)
    
class Struct():
    def __init__(self, name):
        self.name = name
        self.total_size = 0
        self.elements = []

    def __iter__(self):
        for element in self.elements:
            yield element
    
    def add(self, name, size):
        if len(self.name) > 0:
            self.elements.append(StructElement(name, size, self.total_size, f"{self.name}->"))
        else:
            self.elements.append(StructElement(name, size, self.total_size, ""))
        self.total_size += self.elements[-1].size
    
    def find(self, name: str):
        for element in self.elements:
            if element.name == name:
                return element

fp = claripy.BVS("fp", 8*8, explicit_name=True)

# Declare all BVS
file_struct = Struct("")
file_struct.add("_flags", 8*8)
file_struct.add("_IO_read_ptr", 8*8)
file_struct.add("_IO_read_end", 8*8)
file_struct.add("_IO_read_base", 8*8)
file_struct.add("_IO_write_base", 8*8)
file_struct.add("_IO_write_ptr", 8*8)
file_struct.add("_IO_write_end", 8*8)
file_struct.add("_IO_buf_base", 8*8)
file_struct.add("_IO_buf_end", 8*8)
file_struct.add("_IO_save_base", 8*8)
file_struct.add("_IO_backup_base", 8*8)
file_struct.add("_IO_save_end", 8*8)
file_struct.add("_markers", 8*8)
file_struct.add("_chain", 8*8)
file_struct.add("_fileno", 8*4)
file_struct.add("_flags2", 8*4)
file_struct.add("_old_offset", 8*8)
file_struct.add("_cur_column", 8*2)
file_struct.add("_vtable_offset", 8*1)
file_struct.add("_shortbuf", 8*1)
file_struct.add("unknown1", 8*4)
file_struct.add("_lock", 8*8)
file_struct.add("_offset", 8*8)
file_struct.add("_codecvt", 8*8)
file_struct.add("_wide_data", 8*8)
file_struct.add("_freeres_list", 8*8)
file_struct.add("_freeres_buf", 8*8)
file_struct.add("__pad5", 8*8)
file_struct.add("_mode", 8*4)
file_struct.add("_unused2", 8*20)
file_struct.add("vtable", 8*8)
file_struct.add("next_FILE", 8*8)
print(f"Total size for file_struct is {file_struct.total_size//8}")

wide_data = Struct("_wide_data")
wide_data.add("_IO_read_ptr", 8*8),
wide_data.add("_IO_read_end", 8*8),
wide_data.add("_IO_read_base", 8*8),
wide_data.add("_IO_write_base", 8*8),
wide_data.add("_IO_write_ptr", 8*8),
wide_data.add("_IO_write_end", 8*8),
wide_data.add("_IO_buf_base", 8*8),
wide_data.add("_IO_buf_end", 8*8),
wide_data.add("_IO_save_base", 8*8),
wide_data.add("_IO_backup_base", 8*8),
wide_data.add("_IO_save_end", 8*8),
wide_data.add("_IO_state", 8*8),
wide_data.add("_IO_last_state", 8*8),
wide_data.add("__cd_in", 8*56),
wide_data.add("__cd_out", 8*56),
wide_data.add("_shortbuf", 8*4),
wide_data.add("unknown1", 8*4),
wide_data.add("_wide_vtable", 8*8)
print(f"Total size for wide_data is {wide_data.total_size//8}")

codecvt = Struct("_codecvt")
codecvt.add("__cd_in", 8*56)
codecvt.add("__cd_out", 8*56)
print(f"Total size for codecvt is {codecvt.total_size//8}")

# codecvt = Struct("__cd_in")
# codecvt.add("step", 8*8)
# codecvt.add("step_data", 8*48)
# print(f"Total size for codecvt is {codecvt.total_size//8}")

def init_mem(state):
    state.memory.store(FP_ADDR, fp, endness=archinfo.Endness.LE)
    
    for elem in file_struct:
        state.memory.store(FILE_STRUCT_ADDR + (elem.offset // 8), elem.BVS, endness=archinfo.Endness.LE)
    
    for elem in wide_data:
        state.memory.store(WIDE_DATA_ADDR + (elem.offset // 8), elem.BVS, endness=archinfo.Endness.LE)
    
    for elem in codecvt:
        state.memory.store(CODECVT_ADDR + (elem.offset // 8), elem.BVS, endness=archinfo.Endness.LE)

start = time.time()
for name, start_addr, size in target_symbols:
    print(name)
    state = proj.factory.blank_state(addr=start_addr, add_options={angr.options.MEMORY_SYMBOLIC_BYTES_MAP, angr.options.REGION_MAPPING, angr.options.REVERSE_MEMORY_NAME_MAP, angr.options.SYMBOLIC_WRITE_ADDRESSES})
    reg_list = [x for x in state.arch.default_symbolic_registers if x not in ['rip', 'rsp']]
    for reg in reg_list:
        setattr(state.regs, reg, claripy.BVS(f"orig_{reg}", 8*8, explicit_name=True))
    state.stack_push(0x41414141)
    state.regs.rdi = fp
    init_mem(state)

    state.solver.add(fp == FILE_STRUCT_ADDR)
    state.solver.add(file_struct.find("_wide_data").BVS == WIDE_DATA_ADDR)
    state.solver.add(file_struct.find("_codecvt").BVS == CODECVT_ADDR)
    state.solver.add(file_struct.find("vtable").BVS == start_addr)
    
    # Read and write strategies
    state.memory.read_strategies = [SimConcretizationStrategySignedAdd(), SimConcretizationStrategyAnyNamed()]
    # state.memory.write_strategies = [SimConcretizationStrategyAnyNamed()]

    # Wrap into logging strategies
    state.memory.read_strategies = list(map(lambda s: SimConcretizationStrategyLogging(s, True), state.memory.read_strategies))
    state.memory.write_strategies = list(map(lambda s: SimConcretizationStrategyLogging(s, False), state.memory.write_strategies))

    simgr = proj.factory.simgr(state, save_unconstrained=True)
    # simgr.use_technique(angr.exploration_techniques.Veritesting())

    for sym_name, addr, size in symbols:
        if sym_name == "_IO_vtable_check":
            vtable_check = addr
            break

    # Do exploration
    simgr.stashes['avoided'] = []
    simgr.stashes['bad'] = []
    simgr.stashes['unconstrained'] = []
    step = 0
    try:
        while simgr.active:
            lap = time.time()
            simgr.step()
            elapsed_time = time.time() - lap
            simgr.move("active", "deadended", filter_func=lambda s: s.addr == 0x41414141)
            simgr.move("active", "avoided", filter_func=lambda s: s.addr == vtable_check)
            simgr.move("unconstrained", "bad", filter_func=lambda s: s.regs.pc.depth > 1)
            simgr.move("active", "errored", filter_func=lambda s: proj.loader.find_segment_containing(s.addr) is None)
            print(f"\ntime: {elapsed_time}")
            print(simgr)
            step += 1
            if elapsed_time > TIMEOUT:
                break
            if step > MAX_STEP:
                break
    except Exception:
        pass

    # Save results if there are any
    if simgr.unconstrained:
        with open(f"{output_dir}/{name}.pickle", 'wb') as f:
            pickle.dump(simgr.unconstrained, f)

elapsed_time = time.time() - start
print(f"Total exploration time: {elapsed_time}")