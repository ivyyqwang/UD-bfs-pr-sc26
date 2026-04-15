from EFA_v2 import *
def div_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4921317661156713013, 3613187488555131744]
    tran0.writeAction("movir X16 17484")
    tran0.writeAction("slorii X16 X16 12 133")
    tran0.writeAction("slorii X16 X16 12 1708")
    tran0.writeAction("slorii X16 X16 12 418")
    tran0.writeAction("slorii X16 X16 12 565")
    tran0.writeAction("movir X17 12836")
    tran0.writeAction("slorii X17 X17 12 2542")
    tran0.writeAction("slorii X17 X17 12 154")
    tran0.writeAction("slorii X17 X17 12 878")
    tran0.writeAction("slorii X17 X17 12 864")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
