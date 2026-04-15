from EFA_v2 import *
def div_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4030029376774111092, -5279452500844319446]
    tran0.writeAction("movir X16 51218")
    tran0.writeAction("slorii X16 X16 12 1882")
    tran0.writeAction("slorii X16 X16 12 578")
    tran0.writeAction("slorii X16 X16 12 4056")
    tran0.writeAction("slorii X16 X16 12 140")
    tran0.writeAction("movir X17 46779")
    tran0.writeAction("slorii X17 X17 12 2526")
    tran0.writeAction("slorii X17 X17 12 3094")
    tran0.writeAction("slorii X17 X17 12 2566")
    tran0.writeAction("slorii X17 X17 12 3370")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
