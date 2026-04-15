from EFA_v2 import *
def div_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4306140708575008037, -2512340446089448554]
    tran0.writeAction("movir X16 15298")
    tran0.writeAction("slorii X16 X16 12 1986")
    tran0.writeAction("slorii X16 X16 12 2263")
    tran0.writeAction("slorii X16 X16 12 1893")
    tran0.writeAction("slorii X16 X16 12 1317")
    tran0.writeAction("movir X17 56610")
    tran0.writeAction("slorii X17 X17 12 1530")
    tran0.writeAction("slorii X17 X17 12 3291")
    tran0.writeAction("slorii X17 X17 12 4063")
    tran0.writeAction("slorii X17 X17 12 918")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
