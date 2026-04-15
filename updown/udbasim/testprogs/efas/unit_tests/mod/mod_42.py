from EFA_v2 import *
def mod_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5714731644571943219, -4162857505729395008]
    tran0.writeAction("movir X16 45233")
    tran0.writeAction("slorii X16 X16 12 797")
    tran0.writeAction("slorii X16 X16 12 2274")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 3789")
    tran0.writeAction("movir X17 50746")
    tran0.writeAction("slorii X17 X17 12 2290")
    tran0.writeAction("slorii X17 X17 12 1920")
    tran0.writeAction("slorii X17 X17 12 1764")
    tran0.writeAction("slorii X17 X17 12 1728")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
