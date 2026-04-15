from EFA_v2 import *
def subi_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2059890815546609093, -31507]
    tran0.writeAction("movir X16 58217")
    tran0.writeAction("slorii X16 X16 12 3267")
    tran0.writeAction("slorii X16 X16 12 1935")
    tran0.writeAction("slorii X16 X16 12 1043")
    tran0.writeAction("slorii X16 X16 12 571")
    tran0.writeAction("subi X16 X17 -31507")
    tran0.writeAction("yieldt")
    return efa
