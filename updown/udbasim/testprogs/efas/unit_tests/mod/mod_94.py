from EFA_v2 import *
def mod_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6709787769219610151, 2198028185434094187]
    tran0.writeAction("movir X16 41698")
    tran0.writeAction("slorii X16 X16 12 185")
    tran0.writeAction("slorii X16 X16 12 745")
    tran0.writeAction("slorii X16 X16 12 1656")
    tran0.writeAction("slorii X16 X16 12 2521")
    tran0.writeAction("movir X17 7808")
    tran0.writeAction("slorii X17 X17 12 3951")
    tran0.writeAction("slorii X17 X17 12 3375")
    tran0.writeAction("slorii X17 X17 12 391")
    tran0.writeAction("slorii X17 X17 12 2667")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
