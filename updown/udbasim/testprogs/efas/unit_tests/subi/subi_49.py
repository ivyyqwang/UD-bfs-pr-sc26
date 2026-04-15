from EFA_v2 import *
def subi_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1125176676725411062, 7763]
    tran0.writeAction("movir X16 61538")
    tran0.writeAction("slorii X16 X16 12 2332")
    tran0.writeAction("slorii X16 X16 12 1570")
    tran0.writeAction("slorii X16 X16 12 931")
    tran0.writeAction("slorii X16 X16 12 778")
    tran0.writeAction("subi X16 X17 7763")
    tran0.writeAction("yieldt")
    return efa
