from EFA_v2 import *
def div_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1636528254555765941, 2208162547980831659]
    tran0.writeAction("movir X16 5814")
    tran0.writeAction("slorii X16 X16 12 476")
    tran0.writeAction("slorii X16 X16 12 1757")
    tran0.writeAction("slorii X16 X16 12 2811")
    tran0.writeAction("slorii X16 X16 12 3253")
    tran0.writeAction("movir X17 7844")
    tran0.writeAction("slorii X17 X17 12 3970")
    tran0.writeAction("slorii X17 X17 12 854")
    tran0.writeAction("slorii X17 X17 12 2944")
    tran0.writeAction("slorii X17 X17 12 2987")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
