from EFA_v2 import *
def fmul_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7032474165021175096, 10353355266101631193]
    tran0.writeAction("movir X16 24984")
    tran0.writeAction("slorii X16 X16 12 1503")
    tran0.writeAction("slorii X16 X16 12 3666")
    tran0.writeAction("slorii X16 X16 12 814")
    tran0.writeAction("slorii X16 X16 12 3384")
    tran0.writeAction("movir X17 36782")
    tran0.writeAction("slorii X17 X17 12 2076")
    tran0.writeAction("slorii X17 X17 12 661")
    tran0.writeAction("slorii X17 X17 12 1669")
    tran0.writeAction("slorii X17 X17 12 2265")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
