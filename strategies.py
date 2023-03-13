from angr.concretization_strategies import *
import archinfo

class SimConcretizationStrategyLogging(SimConcretizationStrategy):
    def __init__(self, strategy: SimConcretizationStrategy, is_read: bool):
        super().__init__()
        self._strategy = strategy
        self._is_read = is_read

    def _concretize(self, memory, addr, **kwargs):
        answers = self._strategy._concretize(memory, addr, **kwargs)
        if answers is not None:
            if self._is_read:
                print(f"Read strategy {type(self._strategy).__name__} on {addr} gave [{', '.join(map(hex, answers))}]")
            else:
                print(f"Write strategy {type(self._strategy).__name__} on {addr} gave [{', '.join(map(hex, answers))}]")
        return answers


class SimConcretizationStrategyAnyNamed(SimConcretizationStrategy):
    def __init__(self):
        super().__init__()

    def _concretize(self, memory, addr, **kwargs):
        must_create_new = True
        mn, mx = self._range(memory, addr, **kwargs)
        if mn == mx:
            # Check if a variable already exists
            for name, values in memory._name_mapping.items():
                if mn in values:
                    must_create_new = False
                    offset = mn - min(values)
                    if offset == 0:
                        print(f"Target is actually {name}")
                    else:
                        print(f"Target is actually {name}+{offset}")
                    return [mn]
        print(addr)
        # Basic constraints
        child_constraints = (addr > 0x10000000, addr < 0xfffffffffffff000, addr % 8 == 0)
        extra_constraints = kwargs.pop("extra_constraints", None)
        if extra_constraints is not None:
            child_constraints += tuple(extra_constraints)
        target = self._any(memory, addr, extra_constraints=child_constraints, **kwargs)
        # Create new BVS
        old_name = " ".join(repr(addr)[:-1].split(" ")[1:])
        new_name = f"[{old_name}]"
        new_BVS = memory.state.solver.BVS(new_name, 64, explicit_name=True)
        print(f"Creating new BVS {new_name} at address {hex(target)}")
        try:
            memory.store(target, new_BVS, endness=archinfo.Endness.LE)
            # Enforce the address
            memory.state.solver.add(addr == target)
        except Exception as e:
            print(e)
            exit(1)
        return [target]


class SimConcretizationStrategySignedAdd(SimConcretizationStrategy):
    def __init__(self):
        super().__init__()

    def _concretize(self, memory, addr, **kwargs):
        if addr.depth == 2 and addr.op == "__add__":
            if addr.args[0].singlevalued and addr.args[1].symbolic:
                # Swap variable and immediate
                addr.args = (addr.args[1], addr.args[0])
            if addr.args[0].symbolic and addr.args[1].singlevalued:
                # Check if negative argument
                if memory.state.solver.is_true(addr.args[1] >= 1 << (addr.args[1].size()-1)):
                    addr.op = "__sub__"
                    new_value = (1 << addr.args[1].size()) - memory.state.solver.eval(addr.args[1])
                    addr.args = (addr.args[0], memory.state.solver.BVV(new_value, addr.args[1].size()))
                    print("Sign swapped BVS: " + repr(addr))
        return None