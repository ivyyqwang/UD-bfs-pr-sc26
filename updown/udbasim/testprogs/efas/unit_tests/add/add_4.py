from EFA_v2 import *
def add_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6120407717321880784, 5478288639948817618]
    tran0.writeAction("movir X16 21744")
    tran0.writeAction("slorii X16 X16 12 230")
    tran0.writeAction("slorii X16 X16 12 1087")
    tran0.writeAction("slorii X16 X16 12 2171")
    tran0.writeAction("slorii X16 X16 12 1232")
    tran0.writeAction("movir X17 19462")
    tran0.writeAction("slorii X17 X17 12 3239")
    tran0.writeAction("slorii X17 X17 12 3625")
    tran0.writeAction("slorii X17 X17 12 848")
    tran0.writeAction("slorii X17 X17 12 1234")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
