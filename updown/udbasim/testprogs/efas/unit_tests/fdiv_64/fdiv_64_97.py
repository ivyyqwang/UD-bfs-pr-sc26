from EFA_v2 import *
def fdiv_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7107622734384690582, 16105837065183154957]
    tran0.writeAction("movir X16 25251")
    tran0.writeAction("slorii X16 X16 12 1427")
    tran0.writeAction("slorii X16 X16 12 2072")
    tran0.writeAction("slorii X16 X16 12 2007")
    tran0.writeAction("slorii X16 X16 12 1430")
    tran0.writeAction("movir X17 57219")
    tran0.writeAction("slorii X17 X17 12 1751")
    tran0.writeAction("slorii X17 X17 12 2680")
    tran0.writeAction("slorii X17 X17 12 2301")
    tran0.writeAction("slorii X17 X17 12 781")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
