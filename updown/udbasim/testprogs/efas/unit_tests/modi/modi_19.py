from EFA_v2 import *
def modi_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7103474065250664681, 6489]
    tran0.writeAction("movir X16 25236")
    tran0.writeAction("slorii X16 X16 12 2496")
    tran0.writeAction("slorii X16 X16 12 1738")
    tran0.writeAction("slorii X16 X16 12 1908")
    tran0.writeAction("slorii X16 X16 12 233")
    tran0.writeAction("modi X16 X17 6489")
    tran0.writeAction("yieldt")
    return efa
