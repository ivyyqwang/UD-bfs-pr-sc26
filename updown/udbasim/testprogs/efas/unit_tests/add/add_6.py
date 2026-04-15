from EFA_v2 import *
def add_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6626728426657684421, -8548383372615676620]
    tran0.writeAction("movir X16 41993")
    tran0.writeAction("slorii X16 X16 12 537")
    tran0.writeAction("slorii X16 X16 12 2842")
    tran0.writeAction("slorii X16 X16 12 350")
    tran0.writeAction("slorii X16 X16 12 1083")
    tran0.writeAction("movir X17 35166")
    tran0.writeAction("slorii X17 X17 12 169")
    tran0.writeAction("slorii X17 X17 12 3367")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 3380")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
