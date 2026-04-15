from EFA_v2 import *
def fsub_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6157836474123485791, 14628562911943346943]
    tran0.writeAction("movir X16 21877")
    tran0.writeAction("slorii X16 X16 12 122")
    tran0.writeAction("slorii X16 X16 12 1481")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 607")
    tran0.writeAction("movir X17 51971")
    tran0.writeAction("slorii X17 X17 12 391")
    tran0.writeAction("slorii X17 X17 12 1668")
    tran0.writeAction("slorii X17 X17 12 3428")
    tran0.writeAction("slorii X17 X17 12 2815")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
