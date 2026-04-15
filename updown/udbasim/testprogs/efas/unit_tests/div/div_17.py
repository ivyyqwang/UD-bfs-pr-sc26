from EFA_v2 import *
def div_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1275263894419504113, 367559574431035748]
    tran0.writeAction("movir X16 61005")
    tran0.writeAction("slorii X16 X16 12 1443")
    tran0.writeAction("slorii X16 X16 12 3746")
    tran0.writeAction("slorii X16 X16 12 1000")
    tran0.writeAction("slorii X16 X16 12 1039")
    tran0.writeAction("movir X17 1305")
    tran0.writeAction("slorii X17 X17 12 3415")
    tran0.writeAction("slorii X17 X17 12 3147")
    tran0.writeAction("slorii X17 X17 12 3095")
    tran0.writeAction("slorii X17 X17 12 356")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
