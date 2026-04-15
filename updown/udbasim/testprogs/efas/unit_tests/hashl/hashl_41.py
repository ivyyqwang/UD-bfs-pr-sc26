from EFA_v2 import *
def hashl_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4176951797758520739, -596135033190234601]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 50696")
    tran0.writeAction("slorii X17 X17 12 1991")
    tran0.writeAction("slorii X17 X17 12 2154")
    tran0.writeAction("slorii X17 X17 12 2761")
    tran0.writeAction("slorii X17 X17 12 605")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63418")
    tran0.writeAction("slorii X17 X17 12 421")
    tran0.writeAction("slorii X17 X17 12 2180")
    tran0.writeAction("slorii X17 X17 12 2172")
    tran0.writeAction("slorii X17 X17 12 1559")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
