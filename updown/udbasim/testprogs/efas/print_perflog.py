from EFA_v2 import *
def print_perflog():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction(f"jmp forward")
    tran0.writeAction(f"backward: print '%d' X0")
    tran0.writeAction(f"jmp terminate")
    tran0.writeAction(f"forward: print '%d, %d ' X8 X9")
    tran0.writeAction(f"jmp backward")
    tran0.writeAction("terminate: yieldt")
    return efa
