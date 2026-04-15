from EFA_v2 import *
def subi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2447770634991549957, -24281]
    tran0.writeAction("movir X16 8696")
    tran0.writeAction("slorii X16 X16 12 934")
    tran0.writeAction("slorii X16 X16 12 3190")
    tran0.writeAction("slorii X16 X16 12 1243")
    tran0.writeAction("slorii X16 X16 12 3589")
    tran0.writeAction("subi X16 X17 -24281")
    tran0.writeAction("yieldt")
    return efa
