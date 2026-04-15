from EFA_v2 import *
def divi_100():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4671090202238609485, 0]
    tran0.writeAction("movir X16 48940")
    tran0.writeAction("slorii X16 X16 12 3907")
    tran0.writeAction("slorii X16 X16 12 1445")
    tran0.writeAction("slorii X16 X16 12 3113")
    tran0.writeAction("slorii X16 X16 12 1971")
    tran0.writeAction("divi X16 X17 0")
    tran0.writeAction("addi X7 X18 0")
    tran0.writeAction("movrl X4 0(X18) 0 8")
    tran0.writeAction("yieldt")
    return efa
