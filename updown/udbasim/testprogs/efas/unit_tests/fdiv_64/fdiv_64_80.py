from EFA_v2 import *
def fdiv_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6181989010774092045, 5020758122992939741]
    tran0.writeAction("movir X16 21962")
    tran0.writeAction("slorii X16 X16 12 3428")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 2286")
    tran0.writeAction("slorii X16 X16 12 2317")
    tran0.writeAction("movir X17 17837")
    tran0.writeAction("slorii X17 X17 12 1294")
    tran0.writeAction("slorii X17 X17 12 2408")
    tran0.writeAction("slorii X17 X17 12 619")
    tran0.writeAction("slorii X17 X17 12 733")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
