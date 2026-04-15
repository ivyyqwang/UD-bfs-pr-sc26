from EFA_v2 import *
def fcnvt_64_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14548495701429808572]
    tran0.writeAction("movir X16 51686")
    tran0.writeAction("slorii X16 X16 12 2620")
    tran0.writeAction("slorii X16 X16 12 604")
    tran0.writeAction("slorii X16 X16 12 86")
    tran0.writeAction("slorii X16 X16 12 3516")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
