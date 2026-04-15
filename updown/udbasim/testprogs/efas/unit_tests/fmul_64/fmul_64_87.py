from EFA_v2 import *
def fmul_64_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10058062690342434459, 9368559185989213826]
    tran0.writeAction("movir X16 35733")
    tran0.writeAction("slorii X16 X16 12 1707")
    tran0.writeAction("slorii X16 X16 12 2586")
    tran0.writeAction("slorii X16 X16 12 1927")
    tran0.writeAction("slorii X16 X16 12 1691")
    tran0.writeAction("movir X17 33283")
    tran0.writeAction("slorii X17 X17 12 3311")
    tran0.writeAction("slorii X17 X17 12 354")
    tran0.writeAction("slorii X17 X17 12 449")
    tran0.writeAction("slorii X17 X17 12 3714")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
