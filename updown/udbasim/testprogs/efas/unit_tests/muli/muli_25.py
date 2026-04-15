from EFA_v2 import *
def muli_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8868454172584024287, 19090]
    tran0.writeAction("movir X16 34028")
    tran0.writeAction("slorii X16 X16 12 3774")
    tran0.writeAction("slorii X16 X16 12 2760")
    tran0.writeAction("slorii X16 X16 12 1222")
    tran0.writeAction("slorii X16 X16 12 1825")
    tran0.writeAction("muli X16 X17 19090")
    tran0.writeAction("yieldt")
    return efa
