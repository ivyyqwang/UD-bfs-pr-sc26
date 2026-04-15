from EFA_v2 import *
def fdiv_64_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10007837186555628017, 1179342823950715086]
    tran0.writeAction("movir X16 35554")
    tran0.writeAction("slorii X16 X16 12 4014")
    tran0.writeAction("slorii X16 X16 12 1466")
    tran0.writeAction("slorii X16 X16 12 2428")
    tran0.writeAction("slorii X16 X16 12 2545")
    tran0.writeAction("movir X17 4189")
    tran0.writeAction("slorii X17 X17 12 3552")
    tran0.writeAction("slorii X17 X17 12 3273")
    tran0.writeAction("slorii X17 X17 12 4048")
    tran0.writeAction("slorii X17 X17 12 2254")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
