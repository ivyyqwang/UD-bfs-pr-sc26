from EFA_v2 import *
def addi_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2033542524889685536, 2095]
    tran0.writeAction("movir X16 58311")
    tran0.writeAction("slorii X16 X16 12 1661")
    tran0.writeAction("slorii X16 X16 12 2312")
    tran0.writeAction("slorii X16 X16 12 1226")
    tran0.writeAction("slorii X16 X16 12 480")
    tran0.writeAction("addi X16 X17 2095")
    tran0.writeAction("yieldt")
    return efa
