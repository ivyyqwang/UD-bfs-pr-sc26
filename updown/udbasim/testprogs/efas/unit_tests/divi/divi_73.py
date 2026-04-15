from EFA_v2 import *
def divi_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3103625317001607603, -12867]
    tran0.writeAction("movir X16 11026")
    tran0.writeAction("slorii X16 X16 12 1196")
    tran0.writeAction("slorii X16 X16 12 2103")
    tran0.writeAction("slorii X16 X16 12 3235")
    tran0.writeAction("slorii X16 X16 12 2483")
    tran0.writeAction("divi X16 X17 -12867")
    tran0.writeAction("yieldt")
    return efa
