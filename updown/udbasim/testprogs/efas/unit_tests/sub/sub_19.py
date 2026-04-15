from EFA_v2 import *
def sub_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8520686859645183772, -473483561204913108]
    tran0.writeAction("movir X16 30271")
    tran0.writeAction("slorii X16 X16 12 2296")
    tran0.writeAction("slorii X16 X16 12 3559")
    tran0.writeAction("slorii X16 X16 12 2006")
    tran0.writeAction("slorii X16 X16 12 1820")
    tran0.writeAction("movir X17 63853")
    tran0.writeAction("slorii X17 X17 12 3475")
    tran0.writeAction("slorii X17 X17 12 1455")
    tran0.writeAction("slorii X17 X17 12 1614")
    tran0.writeAction("slorii X17 X17 12 3116")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
