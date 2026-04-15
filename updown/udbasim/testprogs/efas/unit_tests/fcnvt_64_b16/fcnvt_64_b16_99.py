from EFA_v2 import *
def fcnvt_64_b16_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17475924911272117764]
    tran0.writeAction("movir X16 62086")
    tran0.writeAction("slorii X16 X16 12 3921")
    tran0.writeAction("slorii X16 X16 12 3465")
    tran0.writeAction("slorii X16 X16 12 3172")
    tran0.writeAction("slorii X16 X16 12 1540")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
