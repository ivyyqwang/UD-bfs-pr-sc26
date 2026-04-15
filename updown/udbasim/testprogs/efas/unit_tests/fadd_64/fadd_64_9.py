from EFA_v2 import *
def fadd_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16221871373377297061, 10469761906408296190]
    tran0.writeAction("movir X16 57631")
    tran0.writeAction("slorii X16 X16 12 2721")
    tran0.writeAction("slorii X16 X16 12 290")
    tran0.writeAction("slorii X16 X16 12 949")
    tran0.writeAction("slorii X16 X16 12 2725")
    tran0.writeAction("movir X17 37196")
    tran0.writeAction("slorii X17 X17 12 271")
    tran0.writeAction("slorii X17 X17 12 2962")
    tran0.writeAction("slorii X17 X17 12 1568")
    tran0.writeAction("slorii X17 X17 12 3838")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
