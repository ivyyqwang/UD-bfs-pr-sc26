from EFA_v2 import *
def add_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1293336825011099219, 4374687904111569015]
    tran0.writeAction("movir X16 60941")
    tran0.writeAction("slorii X16 X16 12 592")
    tran0.writeAction("slorii X16 X16 12 658")
    tran0.writeAction("slorii X16 X16 12 1154")
    tran0.writeAction("slorii X16 X16 12 2477")
    tran0.writeAction("movir X17 15542")
    tran0.writeAction("slorii X17 X17 12 55")
    tran0.writeAction("slorii X17 X17 12 2175")
    tran0.writeAction("slorii X17 X17 12 3146")
    tran0.writeAction("slorii X17 X17 12 2167")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
