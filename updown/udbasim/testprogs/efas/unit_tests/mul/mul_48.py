from EFA_v2 import *
def mul_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7657588235954789162, 1492110854178496168]
    tran0.writeAction("movir X16 38330")
    tran0.writeAction("slorii X16 X16 12 3201")
    tran0.writeAction("slorii X16 X16 12 559")
    tran0.writeAction("slorii X16 X16 12 2886")
    tran0.writeAction("slorii X16 X16 12 1238")
    tran0.writeAction("movir X17 5301")
    tran0.writeAction("slorii X17 X17 12 174")
    tran0.writeAction("slorii X17 X17 12 2708")
    tran0.writeAction("slorii X17 X17 12 3333")
    tran0.writeAction("slorii X17 X17 12 3752")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
