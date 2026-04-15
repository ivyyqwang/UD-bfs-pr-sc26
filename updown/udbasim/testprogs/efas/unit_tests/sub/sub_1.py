from EFA_v2 import *
def sub_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4334887833556878259, -3781786138929177783]
    tran0.writeAction("movir X16 15400")
    tran0.writeAction("slorii X16 X16 12 2520")
    tran0.writeAction("slorii X16 X16 12 1140")
    tran0.writeAction("slorii X16 X16 12 1312")
    tran0.writeAction("slorii X16 X16 12 947")
    tran0.writeAction("movir X17 52100")
    tran0.writeAction("slorii X17 X17 12 1624")
    tran0.writeAction("slorii X17 X17 12 2844")
    tran0.writeAction("slorii X17 X17 12 2581")
    tran0.writeAction("slorii X17 X17 12 2889")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
