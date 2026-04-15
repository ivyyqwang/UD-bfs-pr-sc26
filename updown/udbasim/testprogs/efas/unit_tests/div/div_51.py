from EFA_v2 import *
def div_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9212429996078215187, -7992376226573072698]
    tran0.writeAction("movir X16 32729")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("slorii X16 X16 12 1434")
    tran0.writeAction("slorii X16 X16 12 1619")
    tran0.writeAction("slorii X16 X16 12 19")
    tran0.writeAction("movir X17 37141")
    tran0.writeAction("slorii X17 X17 12 1538")
    tran0.writeAction("slorii X17 X17 12 2775")
    tran0.writeAction("slorii X17 X17 12 3420")
    tran0.writeAction("slorii X17 X17 12 1734")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
