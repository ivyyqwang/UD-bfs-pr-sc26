from EFA_v2 import *
def fcnvt_32_b16_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3435783105]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 204")
    tran0.writeAction("slorii X16 X16 12 3230")
    tran0.writeAction("slorii X16 X16 12 961")
    tran0.writeAction("fcnvt.32.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
