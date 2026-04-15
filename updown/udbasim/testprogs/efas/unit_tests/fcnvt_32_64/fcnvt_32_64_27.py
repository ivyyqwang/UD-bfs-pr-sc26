from EFA_v2 import *
def fcnvt_32_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [591471847]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 35")
    tran0.writeAction("slorii X16 X16 12 1042")
    tran0.writeAction("slorii X16 X16 12 1255")
    tran0.writeAction("fcnvt.32.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
