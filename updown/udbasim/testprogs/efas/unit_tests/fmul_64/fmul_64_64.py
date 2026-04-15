from EFA_v2 import *
def fmul_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2826462450400157350, 15750426049254720780]
    tran0.writeAction("movir X16 10041")
    tran0.writeAction("slorii X16 X16 12 2505")
    tran0.writeAction("slorii X16 X16 12 3991")
    tran0.writeAction("slorii X16 X16 12 333")
    tran0.writeAction("slorii X16 X16 12 3750")
    tran0.writeAction("movir X17 55956")
    tran0.writeAction("slorii X17 X17 12 3088")
    tran0.writeAction("slorii X17 X17 12 2782")
    tran0.writeAction("slorii X17 X17 12 3632")
    tran0.writeAction("slorii X17 X17 12 1292")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
