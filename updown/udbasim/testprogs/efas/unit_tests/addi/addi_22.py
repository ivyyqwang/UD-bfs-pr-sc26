from EFA_v2 import *
def addi_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1322323990057560828, -31654]
    tran0.writeAction("movir X16 4697")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slorii X16 X16 12 1466")
    tran0.writeAction("slorii X16 X16 12 2812")
    tran0.writeAction("addi X16 X17 -31654")
    tran0.writeAction("yieldt")
    return efa
