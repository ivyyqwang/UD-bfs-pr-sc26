from EFA_v2 import *
def fmul_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10318667152681208126, 6998800544722614361]
    tran0.writeAction("movir X16 36659")
    tran0.writeAction("slorii X16 X16 12 1105")
    tran0.writeAction("slorii X16 X16 12 2767")
    tran0.writeAction("slorii X16 X16 12 224")
    tran0.writeAction("slorii X16 X16 12 2366")
    tran0.writeAction("movir X17 24864")
    tran0.writeAction("slorii X17 X17 12 3008")
    tran0.writeAction("slorii X17 X17 12 930")
    tran0.writeAction("slorii X17 X17 12 7")
    tran0.writeAction("slorii X17 X17 12 2137")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
