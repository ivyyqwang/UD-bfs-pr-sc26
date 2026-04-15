from EFA_v2 import *
def fadd_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17255614633505297028, 2198337065229687252]
    tran0.writeAction("movir X16 61304")
    tran0.writeAction("slorii X16 X16 12 1057")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("slorii X16 X16 12 473")
    tran0.writeAction("slorii X16 X16 12 644")
    tran0.writeAction("movir X17 7810")
    tran0.writeAction("slorii X17 X17 12 254")
    tran0.writeAction("slorii X17 X17 12 2525")
    tran0.writeAction("slorii X17 X17 12 2417")
    tran0.writeAction("slorii X17 X17 12 2516")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
