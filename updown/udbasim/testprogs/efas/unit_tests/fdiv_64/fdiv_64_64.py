from EFA_v2 import *
def fdiv_64_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15929913994281799690, 8537060646814267931]
    tran0.writeAction("movir X16 56594")
    tran0.writeAction("slorii X16 X16 12 1734")
    tran0.writeAction("slorii X16 X16 12 163")
    tran0.writeAction("slorii X16 X16 12 2829")
    tran0.writeAction("slorii X16 X16 12 10")
    tran0.writeAction("movir X17 30329")
    tran0.writeAction("slorii X17 X17 12 2998")
    tran0.writeAction("slorii X17 X17 12 3407")
    tran0.writeAction("slorii X17 X17 12 1355")
    tran0.writeAction("slorii X17 X17 12 2587")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
