from EFA_v2 import *
def subi_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1798703328852031755, -30416]
    tran0.writeAction("movir X16 59145")
    tran0.writeAction("slorii X16 X16 12 2957")
    tran0.writeAction("slorii X16 X16 12 2611")
    tran0.writeAction("slorii X16 X16 12 1892")
    tran0.writeAction("slorii X16 X16 12 1781")
    tran0.writeAction("subi X16 X17 -30416")
    tran0.writeAction("yieldt")
    return efa
