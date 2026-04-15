from EFA_v2 import *
def mod_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3955661754308545925, -7650671353524180968]
    tran0.writeAction("movir X16 14053")
    tran0.writeAction("slorii X16 X16 12 1366")
    tran0.writeAction("slorii X16 X16 12 2133")
    tran0.writeAction("slorii X16 X16 12 652")
    tran0.writeAction("slorii X16 X16 12 3461")
    tran0.writeAction("movir X17 38355")
    tran0.writeAction("slorii X17 X17 12 1455")
    tran0.writeAction("slorii X17 X17 12 95")
    tran0.writeAction("slorii X17 X17 12 3826")
    tran0.writeAction("slorii X17 X17 12 2072")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
