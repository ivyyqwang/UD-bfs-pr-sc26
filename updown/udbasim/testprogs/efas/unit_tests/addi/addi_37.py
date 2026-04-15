from EFA_v2 import *
def addi_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2018776492355825383, 25513]
    tran0.writeAction("movir X16 58363")
    tran0.writeAction("slorii X16 X16 12 3543")
    tran0.writeAction("slorii X16 X16 12 2532")
    tran0.writeAction("slorii X16 X16 12 909")
    tran0.writeAction("slorii X16 X16 12 281")
    tran0.writeAction("addi X16 X17 25513")
    tran0.writeAction("yieldt")
    return efa
