from EFA_v2 import *
def add_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8182231149298013281, -1143657526813350419]
    tran0.writeAction("movir X16 36466")
    tran0.writeAction("slorii X16 X16 12 3585")
    tran0.writeAction("slorii X16 X16 12 3835")
    tran0.writeAction("slorii X16 X16 12 3914")
    tran0.writeAction("slorii X16 X16 12 2975")
    tran0.writeAction("movir X17 61472")
    tran0.writeAction("slorii X17 X17 12 3736")
    tran0.writeAction("slorii X17 X17 12 2537")
    tran0.writeAction("slorii X17 X17 12 2410")
    tran0.writeAction("slorii X17 X17 12 1517")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
