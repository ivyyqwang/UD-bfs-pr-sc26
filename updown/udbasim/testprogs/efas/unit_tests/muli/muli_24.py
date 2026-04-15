from EFA_v2 import *
def muli_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-696173264101102632, 1805]
    tran0.writeAction("movir X16 63062")
    tran0.writeAction("slorii X16 X16 12 2849")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("slorii X16 X16 12 530")
    tran0.writeAction("slorii X16 X16 12 3032")
    tran0.writeAction("muli X16 X17 1805")
    tran0.writeAction("yieldt")
    return efa
