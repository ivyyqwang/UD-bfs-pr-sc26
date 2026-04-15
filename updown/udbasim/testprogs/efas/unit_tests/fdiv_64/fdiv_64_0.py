from EFA_v2 import *
def fdiv_64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17744340502203731419, 1093821999648764802]
    tran0.writeAction("movir X16 63040")
    tran0.writeAction("slorii X16 X16 12 2298")
    tran0.writeAction("slorii X16 X16 12 3159")
    tran0.writeAction("slorii X16 X16 12 1760")
    tran0.writeAction("slorii X16 X16 12 3547")
    tran0.writeAction("movir X17 3886")
    tran0.writeAction("slorii X17 X17 12 149")
    tran0.writeAction("slorii X17 X17 12 56")
    tran0.writeAction("slorii X17 X17 12 2343")
    tran0.writeAction("slorii X17 X17 12 898")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
