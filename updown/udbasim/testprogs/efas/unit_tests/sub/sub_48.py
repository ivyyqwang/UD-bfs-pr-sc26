from EFA_v2 import *
def sub_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4743961986576466953, 6257410657316797178]
    tran0.writeAction("movir X16 48682")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("slorii X16 X16 12 1330")
    tran0.writeAction("slorii X16 X16 12 627")
    tran0.writeAction("slorii X16 X16 12 3063")
    tran0.writeAction("movir X17 22230")
    tran0.writeAction("slorii X17 X17 12 3229")
    tran0.writeAction("slorii X17 X17 12 1779")
    tran0.writeAction("slorii X17 X17 12 455")
    tran0.writeAction("slorii X17 X17 12 2810")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
