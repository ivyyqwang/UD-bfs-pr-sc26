from EFA_v2 import *
def sladdii_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1904114696060293715, 13, 705]
    tran0.writeAction("movir X16 6764")
    tran0.writeAction("slorii X16 X16 12 3171")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("slorii X16 X16 12 595")
    tran0.writeAction("sladdii X16 X17 13 705")
    tran0.writeAction("yieldt")
    return efa
