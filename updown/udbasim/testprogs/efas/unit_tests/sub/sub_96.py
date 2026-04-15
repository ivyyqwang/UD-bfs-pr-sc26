from EFA_v2 import *
def sub_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-765405688606259280, -3633227323632686558]
    tran0.writeAction("movir X16 62816")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("slorii X16 X16 12 1245")
    tran0.writeAction("slorii X16 X16 12 2296")
    tran0.writeAction("slorii X16 X16 12 1968")
    tran0.writeAction("movir X17 52628")
    tran0.writeAction("slorii X17 X17 12 751")
    tran0.writeAction("slorii X17 X17 12 4018")
    tran0.writeAction("slorii X17 X17 12 2582")
    tran0.writeAction("slorii X17 X17 12 2594")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
