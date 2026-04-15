from EFA_v2 import *
def hash_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2680070738382713730, 4040852935455508927]
    tran0.writeAction("movir X16 56014")
    tran0.writeAction("slorii X16 X16 12 1949")
    tran0.writeAction("slorii X16 X16 12 3313")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 3198")
    tran0.writeAction("movir X17 14355")
    tran0.writeAction("slorii X17 X17 12 4069")
    tran0.writeAction("slorii X17 X17 12 1503")
    tran0.writeAction("slorii X17 X17 12 1720")
    tran0.writeAction("slorii X17 X17 12 2495")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
