from EFA_v2 import *
def muli_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7996582506276431752, 31402]
    tran0.writeAction("movir X16 37126")
    tran0.writeAction("slorii X16 X16 12 1769")
    tran0.writeAction("slorii X16 X16 12 1032")
    tran0.writeAction("slorii X16 X16 12 1189")
    tran0.writeAction("slorii X16 X16 12 2168")
    tran0.writeAction("muli X16 X17 31402")
    tran0.writeAction("yieldt")
    return efa
