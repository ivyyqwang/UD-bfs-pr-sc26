from EFA_v2 import *
def muli_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7170112086843642090, 5067]
    tran0.writeAction("movir X16 25473")
    tran0.writeAction("slorii X16 X16 12 1455")
    tran0.writeAction("slorii X16 X16 12 1088")
    tran0.writeAction("slorii X16 X16 12 205")
    tran0.writeAction("slorii X16 X16 12 234")
    tran0.writeAction("muli X16 X17 5067")
    tran0.writeAction("yieldt")
    return efa
