from EFA_v2 import *
def fmul_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9805395624029290264, 12252657974327381950]
    tran0.writeAction("movir X16 34835")
    tran0.writeAction("slorii X16 X16 12 3125")
    tran0.writeAction("slorii X16 X16 12 3692")
    tran0.writeAction("slorii X16 X16 12 1783")
    tran0.writeAction("slorii X16 X16 12 3864")
    tran0.writeAction("movir X17 43530")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("slorii X17 X17 12 674")
    tran0.writeAction("slorii X17 X17 12 576")
    tran0.writeAction("slorii X17 X17 12 4030")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
