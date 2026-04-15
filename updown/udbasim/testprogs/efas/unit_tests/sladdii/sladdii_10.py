from EFA_v2 import *
def sladdii_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1014895737189848945, 7, 132]
    tran0.writeAction("movir X16 61930")
    tran0.writeAction("slorii X16 X16 12 1499")
    tran0.writeAction("slorii X16 X16 12 1092")
    tran0.writeAction("slorii X16 X16 12 3034")
    tran0.writeAction("slorii X16 X16 12 2191")
    tran0.writeAction("sladdii X16 X17 7 132")
    tran0.writeAction("yieldt")
    return efa
