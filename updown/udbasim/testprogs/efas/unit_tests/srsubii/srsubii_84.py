from EFA_v2 import *
def srsubii_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4958616853210266403, 8, 165]
    tran0.writeAction("movir X16 17616")
    tran0.writeAction("slorii X16 X16 12 2236")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("slorii X16 X16 12 3535")
    tran0.writeAction("slorii X16 X16 12 2851")
    tran0.writeAction("srsubii X16 X17 8 165")
    tran0.writeAction("yieldt")
    return efa
