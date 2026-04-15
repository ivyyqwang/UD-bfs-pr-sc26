from EFA_v2 import *
def fmul_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18250747648704218053, 16730122765560105126]
    tran0.writeAction("movir X16 64839")
    tran0.writeAction("slorii X16 X16 12 2788")
    tran0.writeAction("slorii X16 X16 12 2614")
    tran0.writeAction("slorii X16 X16 12 1272")
    tran0.writeAction("slorii X16 X16 12 965")
    tran0.writeAction("movir X17 59437")
    tran0.writeAction("slorii X17 X17 12 1376")
    tran0.writeAction("slorii X17 X17 12 1001")
    tran0.writeAction("slorii X17 X17 12 3628")
    tran0.writeAction("slorii X17 X17 12 2214")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
