from EFA_v2 import *
def mul_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1136389211225586135, 6071682886370883850]
    tran0.writeAction("movir X16 61498")
    tran0.writeAction("slorii X16 X16 12 3008")
    tran0.writeAction("slorii X16 X16 12 2178")
    tran0.writeAction("slorii X16 X16 12 1280")
    tran0.writeAction("slorii X16 X16 12 1577")
    tran0.writeAction("movir X17 21570")
    tran0.writeAction("slorii X17 X17 12 3894")
    tran0.writeAction("slorii X17 X17 12 2686")
    tran0.writeAction("slorii X17 X17 12 3911")
    tran0.writeAction("slorii X17 X17 12 2314")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
