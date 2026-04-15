from EFA_v2 import *
def fmul_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10882305015616733066, 4490694164944206715]
    tran0.writeAction("movir X16 38661")
    tran0.writeAction("slorii X16 X16 12 2924")
    tran0.writeAction("slorii X16 X16 12 313")
    tran0.writeAction("slorii X16 X16 12 1175")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("movir X17 15954")
    tran0.writeAction("slorii X17 X17 12 616")
    tran0.writeAction("slorii X17 X17 12 3296")
    tran0.writeAction("slorii X17 X17 12 1715")
    tran0.writeAction("slorii X17 X17 12 2939")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
