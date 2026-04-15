from EFA_v2 import *
def srsubii_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6193702930879448201, 10, 678]
    tran0.writeAction("movir X16 43531")
    tran0.writeAction("slorii X16 X16 12 2240")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 2599")
    tran0.writeAction("slorii X16 X16 12 2935")
    tran0.writeAction("srsubii X16 X17 10 678")
    tran0.writeAction("yieldt")
    return efa
