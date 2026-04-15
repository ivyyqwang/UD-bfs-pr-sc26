from EFA_v2 import *
def fcnvt_64_32_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14001672957377163958]
    tran0.writeAction("movir X16 49743")
    tran0.writeAction("slorii X16 X16 12 3829")
    tran0.writeAction("slorii X16 X16 12 3813")
    tran0.writeAction("slorii X16 X16 12 2699")
    tran0.writeAction("slorii X16 X16 12 694")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
