from EFA_v2 import *
def divi_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3176487569775010517, -25815]
    tran0.writeAction("movir X16 54250")
    tran0.writeAction("slorii X16 X16 12 3478")
    tran0.writeAction("slorii X16 X16 12 658")
    tran0.writeAction("slorii X16 X16 12 477")
    tran0.writeAction("slorii X16 X16 12 3371")
    tran0.writeAction("divi X16 X17 -25815")
    tran0.writeAction("yieldt")
    return efa
