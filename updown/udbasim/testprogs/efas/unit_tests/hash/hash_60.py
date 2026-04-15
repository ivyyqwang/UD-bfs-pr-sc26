from EFA_v2 import *
def hash_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-35195929256180588, -2273302334048660150]
    tran0.writeAction("movir X16 65410")
    tran0.writeAction("slorii X16 X16 12 3927")
    tran0.writeAction("slorii X16 X16 12 3363")
    tran0.writeAction("slorii X16 X16 12 596")
    tran0.writeAction("slorii X16 X16 12 1172")
    tran0.writeAction("movir X17 57459")
    tran0.writeAction("slorii X17 X17 12 2489")
    tran0.writeAction("slorii X17 X17 12 599")
    tran0.writeAction("slorii X17 X17 12 3945")
    tran0.writeAction("slorii X17 X17 12 1354")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
