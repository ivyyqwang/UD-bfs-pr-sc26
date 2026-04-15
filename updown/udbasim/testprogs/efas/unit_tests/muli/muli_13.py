from EFA_v2 import *
def muli_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7152431972983940856, -5012]
    tran0.writeAction("movir X16 40125")
    tran0.writeAction("slorii X16 X16 12 1872")
    tran0.writeAction("slorii X16 X16 12 1034")
    tran0.writeAction("slorii X16 X16 12 597")
    tran0.writeAction("slorii X16 X16 12 2312")
    tran0.writeAction("muli X16 X17 -5012")
    tran0.writeAction("yieldt")
    return efa
