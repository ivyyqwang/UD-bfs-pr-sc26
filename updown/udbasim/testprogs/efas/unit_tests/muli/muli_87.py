from EFA_v2 import *
def muli_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5691206609756132882, 13548]
    tran0.writeAction("movir X16 45316")
    tran0.writeAction("slorii X16 X16 12 3163")
    tran0.writeAction("slorii X16 X16 12 3554")
    tran0.writeAction("slorii X16 X16 12 534")
    tran0.writeAction("slorii X16 X16 12 2542")
    tran0.writeAction("muli X16 X17 13548")
    tran0.writeAction("yieldt")
    return efa
