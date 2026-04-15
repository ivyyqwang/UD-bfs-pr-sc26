from EFA_v2 import *
def fadd_64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12573089969601615688, 12272421039501717831]
    tran0.writeAction("movir X16 44668")
    tran0.writeAction("slorii X16 X16 12 2411")
    tran0.writeAction("slorii X16 X16 12 1623")
    tran0.writeAction("slorii X16 X16 12 537")
    tran0.writeAction("slorii X16 X16 12 1864")
    tran0.writeAction("movir X17 43600")
    tran0.writeAction("slorii X17 X17 12 1630")
    tran0.writeAction("slorii X17 X17 12 2513")
    tran0.writeAction("slorii X17 X17 12 2171")
    tran0.writeAction("slorii X17 X17 12 327")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
