from EFA_v2 import *
def mod_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7252980711122215292, -3757438917972209028]
    tran0.writeAction("movir X16 25767")
    tran0.writeAction("slorii X16 X16 12 3128")
    tran0.writeAction("slorii X16 X16 12 1889")
    tran0.writeAction("slorii X16 X16 12 818")
    tran0.writeAction("slorii X16 X16 12 380")
    tran0.writeAction("movir X17 52186")
    tran0.writeAction("slorii X17 X17 12 3667")
    tran0.writeAction("slorii X17 X17 12 1597")
    tran0.writeAction("slorii X17 X17 12 157")
    tran0.writeAction("slorii X17 X17 12 636")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
