from EFA_v2 import *
def div_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3529353409160992692, 6394036039766064905]
    tran0.writeAction("movir X16 52997")
    tran0.writeAction("slorii X16 X16 12 892")
    tran0.writeAction("slorii X16 X16 12 1552")
    tran0.writeAction("slorii X16 X16 12 594")
    tran0.writeAction("slorii X16 X16 12 2124")
    tran0.writeAction("movir X17 22716")
    tran0.writeAction("slorii X17 X17 12 734")
    tran0.writeAction("slorii X17 X17 12 1711")
    tran0.writeAction("slorii X17 X17 12 1235")
    tran0.writeAction("slorii X17 X17 12 3849")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
