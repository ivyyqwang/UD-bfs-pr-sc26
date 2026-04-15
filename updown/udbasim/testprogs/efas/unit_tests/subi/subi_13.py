from EFA_v2 import *
def subi_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-506166790032412887, 31243]
    tran0.writeAction("movir X16 63737")
    tran0.writeAction("slorii X16 X16 12 3007")
    tran0.writeAction("slorii X16 X16 12 3195")
    tran0.writeAction("slorii X16 X16 12 74")
    tran0.writeAction("slorii X16 X16 12 3881")
    tran0.writeAction("subi X16 X17 31243")
    tran0.writeAction("yieldt")
    return efa
