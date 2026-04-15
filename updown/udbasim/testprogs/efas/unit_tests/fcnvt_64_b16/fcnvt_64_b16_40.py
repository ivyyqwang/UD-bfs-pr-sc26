from EFA_v2 import *
def fcnvt_64_b16_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [213094872819189812]
    tran0.writeAction("movir X16 757")
    tran0.writeAction("slorii X16 X16 12 266")
    tran0.writeAction("slorii X16 X16 12 2149")
    tran0.writeAction("slorii X16 X16 12 3460")
    tran0.writeAction("slorii X16 X16 12 2100")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
