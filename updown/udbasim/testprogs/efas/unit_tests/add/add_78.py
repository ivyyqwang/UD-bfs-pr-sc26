from EFA_v2 import *
def add_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3246098069335384061, -4367807689779132460]
    tran0.writeAction("movir X16 54003")
    tran0.writeAction("slorii X16 X16 12 2224")
    tran0.writeAction("slorii X16 X16 12 295")
    tran0.writeAction("slorii X16 X16 12 750")
    tran0.writeAction("slorii X16 X16 12 3")
    tran0.writeAction("movir X17 50018")
    tran0.writeAction("slorii X17 X17 12 1760")
    tran0.writeAction("slorii X17 X17 12 3131")
    tran0.writeAction("slorii X17 X17 12 2028")
    tran0.writeAction("slorii X17 X17 12 2004")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
