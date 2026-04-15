from EFA_v2 import *
def mul_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6990963911456539448, 8863721479016837562]
    tran0.writeAction("movir X16 40699")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 3260")
    tran0.writeAction("slorii X16 X16 12 235")
    tran0.writeAction("slorii X16 X16 12 3272")
    tran0.writeAction("movir X17 31490")
    tran0.writeAction("slorii X17 X17 12 1083")
    tran0.writeAction("slorii X17 X17 12 2336")
    tran0.writeAction("slorii X17 X17 12 3271")
    tran0.writeAction("slorii X17 X17 12 442")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
