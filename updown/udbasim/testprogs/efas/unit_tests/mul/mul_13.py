from EFA_v2 import *
def mul_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3919601909436317578, 2032634345593039253]
    tran0.writeAction("movir X16 13925")
    tran0.writeAction("slorii X16 X16 12 914")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 3663")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("movir X17 7221")
    tran0.writeAction("slorii X17 X17 12 1506")
    tran0.writeAction("slorii X17 X17 12 2815")
    tran0.writeAction("slorii X17 X17 12 1358")
    tran0.writeAction("slorii X17 X17 12 2453")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
