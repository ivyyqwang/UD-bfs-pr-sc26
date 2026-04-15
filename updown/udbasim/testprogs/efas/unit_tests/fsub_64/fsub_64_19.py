from EFA_v2 import *
def fsub_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12233577143380153172, 13760826530456298068]
    tran0.writeAction("movir X16 43462")
    tran0.writeAction("slorii X16 X16 12 1625")
    tran0.writeAction("slorii X16 X16 12 2171")
    tran0.writeAction("slorii X16 X16 12 2097")
    tran0.writeAction("slorii X16 X16 12 852")
    tran0.writeAction("movir X17 48888")
    tran0.writeAction("slorii X17 X17 12 1133")
    tran0.writeAction("slorii X17 X17 12 587")
    tran0.writeAction("slorii X17 X17 12 2534")
    tran0.writeAction("slorii X17 X17 12 596")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
