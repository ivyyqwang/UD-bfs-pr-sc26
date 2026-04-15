from EFA_v2 import *
def fsub_64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14149578818726828253, 9880237523681678629]
    tran0.writeAction("movir X16 50269")
    tran0.writeAction("slorii X16 X16 12 1647")
    tran0.writeAction("slorii X16 X16 12 1995")
    tran0.writeAction("slorii X16 X16 12 2473")
    tran0.writeAction("slorii X16 X16 12 2269")
    tran0.writeAction("movir X17 35101")
    tran0.writeAction("slorii X17 X17 12 2682")
    tran0.writeAction("slorii X17 X17 12 3607")
    tran0.writeAction("slorii X17 X17 12 2177")
    tran0.writeAction("slorii X17 X17 12 1317")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
