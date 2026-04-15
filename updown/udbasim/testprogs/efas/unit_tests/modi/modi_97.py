from EFA_v2 import *
def modi_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2419260327996521793, -14032]
    tran0.writeAction("movir X16 8594")
    tran0.writeAction("slorii X16 X16 12 3847")
    tran0.writeAction("slorii X16 X16 12 853")
    tran0.writeAction("slorii X16 X16 12 1751")
    tran0.writeAction("slorii X16 X16 12 3393")
    tran0.writeAction("modi X16 X17 -14032")
    tran0.writeAction("yieldt")
    return efa
