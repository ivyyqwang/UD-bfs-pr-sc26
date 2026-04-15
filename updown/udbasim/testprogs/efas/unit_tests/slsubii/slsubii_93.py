from EFA_v2 import *
def slsubii_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7367283273729621599, 13, 1755]
    tran0.writeAction("movir X16 26173")
    tran0.writeAction("slorii X16 X16 12 3473")
    tran0.writeAction("slorii X16 X16 12 2714")
    tran0.writeAction("slorii X16 X16 12 1355")
    tran0.writeAction("slorii X16 X16 12 3679")
    tran0.writeAction("slsubii X16 X17 13 1755")
    tran0.writeAction("yieldt")
    return efa
