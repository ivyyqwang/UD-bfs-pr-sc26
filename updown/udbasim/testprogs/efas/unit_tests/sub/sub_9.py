from EFA_v2 import *
def sub_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-143120692555779879, 5654347674610552814]
    tran0.writeAction("movir X16 65027")
    tran0.writeAction("slorii X16 X16 12 2183")
    tran0.writeAction("slorii X16 X16 12 3336")
    tran0.writeAction("slorii X16 X16 12 839")
    tran0.writeAction("slorii X16 X16 12 217")
    tran0.writeAction("movir X17 20088")
    tran0.writeAction("slorii X17 X17 12 1140")
    tran0.writeAction("slorii X17 X17 12 133")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("slorii X17 X17 12 4078")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
