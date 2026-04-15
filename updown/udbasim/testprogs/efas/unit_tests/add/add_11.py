from EFA_v2 import *
def add_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6037079074483791634, 1970128692795540144]
    tran0.writeAction("movir X16 44087")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 332")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 2286")
    tran0.writeAction("movir X17 6999")
    tran0.writeAction("slorii X17 X17 12 1241")
    tran0.writeAction("slorii X17 X17 12 2975")
    tran0.writeAction("slorii X17 X17 12 3616")
    tran0.writeAction("slorii X17 X17 12 688")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
