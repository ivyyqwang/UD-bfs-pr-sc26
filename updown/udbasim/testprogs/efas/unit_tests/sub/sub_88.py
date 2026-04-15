from EFA_v2 import *
def sub_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5862851199557659789, -8831474069345197725]
    tran0.writeAction("movir X16 44706")
    tran0.writeAction("slorii X16 X16 12 3966")
    tran0.writeAction("slorii X16 X16 12 1423")
    tran0.writeAction("slorii X16 X16 12 1609")
    tran0.writeAction("slorii X16 X16 12 883")
    tran0.writeAction("movir X17 34160")
    tran0.writeAction("slorii X17 X17 12 1234")
    tran0.writeAction("slorii X17 X17 12 5")
    tran0.writeAction("slorii X17 X17 12 2482")
    tran0.writeAction("slorii X17 X17 12 355")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
