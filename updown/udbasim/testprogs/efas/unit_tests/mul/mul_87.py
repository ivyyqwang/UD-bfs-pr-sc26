from EFA_v2 import *
def mul_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5104660821933765750, 4773836428543303870]
    tran0.writeAction("movir X16 47400")
    tran0.writeAction("slorii X16 X16 12 2464")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 3212")
    tran0.writeAction("slorii X16 X16 12 2954")
    tran0.writeAction("movir X17 16960")
    tran0.writeAction("slorii X17 X17 12 303")
    tran0.writeAction("slorii X17 X17 12 91")
    tran0.writeAction("slorii X17 X17 12 586")
    tran0.writeAction("slorii X17 X17 12 190")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
