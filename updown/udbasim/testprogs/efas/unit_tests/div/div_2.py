from EFA_v2 import *
def div_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1615271653126760105, -7518306539472071329]
    tran0.writeAction("movir X16 59797")
    tran0.writeAction("slorii X16 X16 12 1647")
    tran0.writeAction("slorii X16 X16 12 3411")
    tran0.writeAction("slorii X16 X16 12 2545")
    tran0.writeAction("slorii X16 X16 12 2391")
    tran0.writeAction("movir X17 38825")
    tran0.writeAction("slorii X17 X17 12 2496")
    tran0.writeAction("slorii X17 X17 12 2362")
    tran0.writeAction("slorii X17 X17 12 1109")
    tran0.writeAction("slorii X17 X17 12 1375")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
