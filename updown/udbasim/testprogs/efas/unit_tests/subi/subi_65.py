from EFA_v2 import *
def subi_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1839175855185314422, 23309]
    tran0.writeAction("movir X16 6534")
    tran0.writeAction("slorii X16 X16 12 267")
    tran0.writeAction("slorii X16 X16 12 551")
    tran0.writeAction("slorii X16 X16 12 3260")
    tran0.writeAction("slorii X16 X16 12 630")
    tran0.writeAction("subi X16 X17 23309")
    tran0.writeAction("yieldt")
    return efa
