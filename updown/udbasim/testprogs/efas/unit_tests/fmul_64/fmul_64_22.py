from EFA_v2 import *
def fmul_64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7458033682585476418, 4328922655146986483]
    tran0.writeAction("movir X16 26496")
    tran0.writeAction("slorii X16 X16 12 1057")
    tran0.writeAction("slorii X16 X16 12 3765")
    tran0.writeAction("slorii X16 X16 12 1661")
    tran0.writeAction("slorii X16 X16 12 3394")
    tran0.writeAction("movir X17 15379")
    tran0.writeAction("slorii X17 X17 12 1731")
    tran0.writeAction("slorii X17 X17 12 2080")
    tran0.writeAction("slorii X17 X17 12 724")
    tran0.writeAction("slorii X17 X17 12 3059")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
