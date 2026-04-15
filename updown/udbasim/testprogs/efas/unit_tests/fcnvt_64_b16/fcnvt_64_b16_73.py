from EFA_v2 import *
def fcnvt_64_b16_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9494878250671548967]
    tran0.writeAction("movir X16 33732")
    tran0.writeAction("slorii X16 X16 12 2391")
    tran0.writeAction("slorii X16 X16 12 1668")
    tran0.writeAction("slorii X16 X16 12 3522")
    tran0.writeAction("slorii X16 X16 12 2599")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
