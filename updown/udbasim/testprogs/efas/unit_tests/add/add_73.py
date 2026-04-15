from EFA_v2 import *
def add_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2271367041853155532, -852895570989515737]
    tran0.writeAction("movir X16 8069")
    tran0.writeAction("slorii X16 X16 12 2116")
    tran0.writeAction("slorii X16 X16 12 2644")
    tran0.writeAction("slorii X16 X16 12 766")
    tran0.writeAction("slorii X16 X16 12 2252")
    tran0.writeAction("movir X17 62505")
    tran0.writeAction("slorii X17 X17 12 3711")
    tran0.writeAction("slorii X17 X17 12 3900")
    tran0.writeAction("slorii X17 X17 12 2727")
    tran0.writeAction("slorii X17 X17 12 3111")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
