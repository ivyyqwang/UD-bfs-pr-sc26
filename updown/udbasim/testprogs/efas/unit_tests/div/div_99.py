from EFA_v2 import *
def div_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3572084471772591916, 4928200768239094551]
    tran0.writeAction("movir X16 12690")
    tran0.writeAction("slorii X16 X16 12 2430")
    tran0.writeAction("slorii X16 X16 12 1727")
    tran0.writeAction("slorii X16 X16 12 2843")
    tran0.writeAction("slorii X16 X16 12 1836")
    tran0.writeAction("movir X17 17508")
    tran0.writeAction("slorii X17 X17 12 1991")
    tran0.writeAction("slorii X17 X17 12 3308")
    tran0.writeAction("slorii X17 X17 12 2860")
    tran0.writeAction("slorii X17 X17 12 2839")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
