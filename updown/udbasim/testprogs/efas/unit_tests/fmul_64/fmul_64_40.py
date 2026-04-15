from EFA_v2 import *
def fmul_64_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7818468428318999530, 7404730787506022070]
    tran0.writeAction("movir X16 27776")
    tran0.writeAction("slorii X16 X16 12 3193")
    tran0.writeAction("slorii X16 X16 12 3213")
    tran0.writeAction("slorii X16 X16 12 2296")
    tran0.writeAction("slorii X16 X16 12 1002")
    tran0.writeAction("movir X17 26306")
    tran0.writeAction("slorii X17 X17 12 3638")
    tran0.writeAction("slorii X17 X17 12 2902")
    tran0.writeAction("slorii X17 X17 12 2846")
    tran0.writeAction("slorii X17 X17 12 1718")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
