from EFA_v2 import *
def mod_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6586290263597020626, -7093416028259921717]
    tran0.writeAction("movir X16 23399")
    tran0.writeAction("slorii X16 X16 12 833")
    tran0.writeAction("slorii X16 X16 12 2397")
    tran0.writeAction("slorii X16 X16 12 1287")
    tran0.writeAction("slorii X16 X16 12 1490")
    tran0.writeAction("movir X17 40335")
    tran0.writeAction("slorii X17 X17 12 507")
    tran0.writeAction("slorii X17 X17 12 1135")
    tran0.writeAction("slorii X17 X17 12 2069")
    tran0.writeAction("slorii X17 X17 12 203")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
