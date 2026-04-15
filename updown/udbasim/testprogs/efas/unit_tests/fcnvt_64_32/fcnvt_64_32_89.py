from EFA_v2 import *
def fcnvt_64_32_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6610063996926600346]
    tran0.writeAction("movir X16 23483")
    tran0.writeAction("slorii X16 X16 12 2722")
    tran0.writeAction("slorii X16 X16 12 3839")
    tran0.writeAction("slorii X16 X16 12 1674")
    tran0.writeAction("slorii X16 X16 12 1178")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
