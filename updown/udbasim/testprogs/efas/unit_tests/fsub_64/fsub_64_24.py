from EFA_v2 import *
def fsub_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15671692614119654417, 8690795190590383125]
    tran0.writeAction("movir X16 55677")
    tran0.writeAction("slorii X16 X16 12 150")
    tran0.writeAction("slorii X16 X16 12 1661")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 1041")
    tran0.writeAction("movir X17 30875")
    tran0.writeAction("slorii X17 X17 12 3714")
    tran0.writeAction("slorii X17 X17 12 3606")
    tran0.writeAction("slorii X17 X17 12 3330")
    tran0.writeAction("slorii X17 X17 12 1045")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
