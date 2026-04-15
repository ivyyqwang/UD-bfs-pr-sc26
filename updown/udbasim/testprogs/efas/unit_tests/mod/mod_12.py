from EFA_v2 import *
def mod_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1668661261277606895, 582005670954686945]
    tran0.writeAction("movir X16 59607")
    tran0.writeAction("slorii X16 X16 12 2966")
    tran0.writeAction("slorii X16 X16 12 3199")
    tran0.writeAction("slorii X16 X16 12 380")
    tran0.writeAction("slorii X16 X16 12 3089")
    tran0.writeAction("movir X17 2067")
    tran0.writeAction("slorii X17 X17 12 2865")
    tran0.writeAction("slorii X17 X17 12 762")
    tran0.writeAction("slorii X17 X17 12 2117")
    tran0.writeAction("slorii X17 X17 12 2529")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
