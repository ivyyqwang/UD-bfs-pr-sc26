from EFA_v2 import *
def div_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3483791837459432640, -3316226137962848934]
    tran0.writeAction("movir X16 12376")
    tran0.writeAction("slorii X16 X16 12 3747")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 716")
    tran0.writeAction("slorii X16 X16 12 1216")
    tran0.writeAction("movir X17 53754")
    tran0.writeAction("slorii X17 X17 12 1630")
    tran0.writeAction("slorii X17 X17 12 1483")
    tran0.writeAction("slorii X17 X17 12 3517")
    tran0.writeAction("slorii X17 X17 12 3418")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
