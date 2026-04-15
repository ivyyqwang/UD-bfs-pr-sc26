from EFA_v2 import *
def slsubii_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7502642578831071211, 12, 125]
    tran0.writeAction("movir X16 38881")
    tran0.writeAction("slorii X16 X16 12 1061")
    tran0.writeAction("slorii X16 X16 12 836")
    tran0.writeAction("slorii X16 X16 12 218")
    tran0.writeAction("slorii X16 X16 12 2069")
    tran0.writeAction("slsubii X16 X17 12 125")
    tran0.writeAction("yieldt")
    return efa
