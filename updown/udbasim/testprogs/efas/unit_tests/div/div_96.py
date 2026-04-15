from EFA_v2 import *
def div_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8625749518171649928, 8583322634557061561]
    tran0.writeAction("movir X16 34891")
    tran0.writeAction("slorii X16 X16 12 744")
    tran0.writeAction("slorii X16 X16 12 943")
    tran0.writeAction("slorii X16 X16 12 3612")
    tran0.writeAction("slorii X16 X16 12 2168")
    tran0.writeAction("movir X17 30494")
    tran0.writeAction("slorii X17 X17 12 359")
    tran0.writeAction("slorii X17 X17 12 1457")
    tran0.writeAction("slorii X17 X17 12 1407")
    tran0.writeAction("slorii X17 X17 12 2489")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
