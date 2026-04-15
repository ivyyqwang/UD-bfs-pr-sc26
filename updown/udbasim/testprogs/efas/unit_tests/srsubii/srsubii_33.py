from EFA_v2 import *
def srsubii_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1475005518600227644, 2, 1870]
    tran0.writeAction("movir X16 60295")
    tran0.writeAction("slorii X16 X16 12 2980")
    tran0.writeAction("slorii X16 X16 12 2998")
    tran0.writeAction("slorii X16 X16 12 379")
    tran0.writeAction("slorii X16 X16 12 1220")
    tran0.writeAction("srsubii X16 X17 2 1870")
    tran0.writeAction("yieldt")
    return efa
