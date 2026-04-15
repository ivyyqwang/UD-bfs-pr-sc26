from EFA_v2 import *
def hash_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-384391920952028080, 5542240977579899911]
    tran0.writeAction("movir X16 64170")
    tran0.writeAction("slorii X16 X16 12 1497")
    tran0.writeAction("slorii X16 X16 12 1441")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("slorii X16 X16 12 1104")
    tran0.writeAction("movir X17 19689")
    tran0.writeAction("slorii X17 X17 12 4076")
    tran0.writeAction("slorii X17 X17 12 3608")
    tran0.writeAction("slorii X17 X17 12 1079")
    tran0.writeAction("slorii X17 X17 12 3079")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
