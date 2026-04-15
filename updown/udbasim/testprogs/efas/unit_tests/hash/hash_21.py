from EFA_v2 import *
def hash_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6389627599165404288, 6860047941935381283]
    tran0.writeAction("movir X16 22700")
    tran0.writeAction("slorii X16 X16 12 2119")
    tran0.writeAction("slorii X16 X16 12 671")
    tran0.writeAction("slorii X16 X16 12 1171")
    tran0.writeAction("slorii X16 X16 12 1152")
    tran0.writeAction("movir X17 24371")
    tran0.writeAction("slorii X17 X17 12 3220")
    tran0.writeAction("slorii X17 X17 12 465")
    tran0.writeAction("slorii X17 X17 12 851")
    tran0.writeAction("slorii X17 X17 12 2851")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
