from EFA_v2 import *
def muli_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8683115592106361990, -17641]
    tran0.writeAction("movir X16 30848")
    tran0.writeAction("slorii X16 X16 12 2554")
    tran0.writeAction("slorii X16 X16 12 59")
    tran0.writeAction("slorii X16 X16 12 636")
    tran0.writeAction("slorii X16 X16 12 1158")
    tran0.writeAction("muli X16 X17 -17641")
    tran0.writeAction("yieldt")
    return efa
