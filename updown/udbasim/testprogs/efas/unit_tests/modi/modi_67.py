from EFA_v2 import *
def modi_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8072289547330174467, -3867]
    tran0.writeAction("movir X16 28678")
    tran0.writeAction("slorii X16 X16 12 2185")
    tran0.writeAction("slorii X16 X16 12 784")
    tran0.writeAction("slorii X16 X16 12 2923")
    tran0.writeAction("slorii X16 X16 12 3587")
    tran0.writeAction("modi X16 X17 -3867")
    tran0.writeAction("yieldt")
    return efa
