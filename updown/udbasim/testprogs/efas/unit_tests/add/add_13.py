from EFA_v2 import *
def add_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [887828735888407023, -1131679912863642099]
    tran0.writeAction("movir X16 3154")
    tran0.writeAction("slorii X16 X16 12 824")
    tran0.writeAction("slorii X16 X16 12 2056")
    tran0.writeAction("slorii X16 X16 12 51")
    tran0.writeAction("slorii X16 X16 12 2543")
    tran0.writeAction("movir X17 61515")
    tran0.writeAction("slorii X17 X17 12 1905")
    tran0.writeAction("slorii X17 X17 12 3450")
    tran0.writeAction("slorii X17 X17 12 1300")
    tran0.writeAction("slorii X17 X17 12 3597")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
