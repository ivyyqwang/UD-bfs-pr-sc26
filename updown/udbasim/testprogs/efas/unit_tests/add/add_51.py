from EFA_v2 import *
def add_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3266942753321656950, 4778016238249054345]
    tran0.writeAction("movir X16 11606")
    tran0.writeAction("slorii X16 X16 12 2098")
    tran0.writeAction("slorii X16 X16 12 9")
    tran0.writeAction("slorii X16 X16 12 1122")
    tran0.writeAction("slorii X16 X16 12 630")
    tran0.writeAction("movir X17 16974")
    tran0.writeAction("slorii X17 X17 12 3783")
    tran0.writeAction("slorii X17 X17 12 1059")
    tran0.writeAction("slorii X17 X17 12 3617")
    tran0.writeAction("slorii X17 X17 12 137")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
