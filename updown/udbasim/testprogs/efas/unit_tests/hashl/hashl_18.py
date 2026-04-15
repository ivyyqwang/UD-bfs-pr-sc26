from EFA_v2 import *
def hashl_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1582042349713419989, 7900983129024062393]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 59915")
    tran0.writeAction("slorii X17 X17 12 1869")
    tran0.writeAction("slorii X17 X17 12 3437")
    tran0.writeAction("slorii X17 X17 12 2897")
    tran0.writeAction("slorii X17 X17 12 299")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 28069")
    tran0.writeAction("slorii X17 X17 12 3812")
    tran0.writeAction("slorii X17 X17 12 2925")
    tran0.writeAction("slorii X17 X17 12 3414")
    tran0.writeAction("slorii X17 X17 12 953")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
