from EFA_v2 import *
def sub_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5456937418141178491, -175874536265946253]
    tran0.writeAction("movir X16 19386")
    tran0.writeAction("slorii X16 X16 12 3834")
    tran0.writeAction("slorii X16 X16 12 2929")
    tran0.writeAction("slorii X16 X16 12 3449")
    tran0.writeAction("slorii X16 X16 12 2683")
    tran0.writeAction("movir X17 64911")
    tran0.writeAction("slorii X17 X17 12 688")
    tran0.writeAction("slorii X17 X17 12 2692")
    tran0.writeAction("slorii X17 X17 12 3406")
    tran0.writeAction("slorii X17 X17 12 2931")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
