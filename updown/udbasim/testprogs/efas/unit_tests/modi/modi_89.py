from EFA_v2 import *
def modi_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3676195275056402007, -6359]
    tran0.writeAction("movir X16 13060")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 22")
    tran0.writeAction("slorii X16 X16 12 2892")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("modi X16 X17 -6359")
    tran0.writeAction("yieldt")
    return efa
