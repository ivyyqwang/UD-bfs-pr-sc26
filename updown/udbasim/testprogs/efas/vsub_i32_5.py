from EFA_v2 import *
def vsub_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1425570473, 1602927403, -1502645533, 2025027051, 1591668918, 1652015884, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1528")
    tran0.writeAction("slorii X19 X19 12 2747")
    tran0.writeAction("slorii X19 X19 8 43")
    tran0.writeAction("slorii X19 X19 12 1359")
    tran0.writeAction("slorii X19 X19 12 2170")
    tran0.writeAction("slorii X19 X19 8 169")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1931")
    tran0.writeAction("slorii X17 X17 12 885")
    tran0.writeAction("slorii X17 X17 8 235")
    tran0.writeAction("slorii X17 X17 12 2662")
    tran0.writeAction("slorii X17 X17 12 3954")
    tran0.writeAction("slorii X17 X17 8 227")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1575")
    tran0.writeAction("slorii X18 X18 12 1987")
    tran0.writeAction("slorii X18 X18 8 12")
    tran0.writeAction("slorii X18 X18 12 1517")
    tran0.writeAction("slorii X18 X18 12 3824")
    tran0.writeAction("slorii X18 X18 8 182")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
