from EFA_v2 import *
def muli_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2482202824433748305, 19469]
    tran0.writeAction("movir X16 56717")
    tran0.writeAction("slorii X16 X16 12 1818")
    tran0.writeAction("slorii X16 X16 12 3765")
    tran0.writeAction("slorii X16 X16 12 635")
    tran0.writeAction("slorii X16 X16 12 1711")
    tran0.writeAction("muli X16 X17 19469")
    tran0.writeAction("yieldt")
    return efa
