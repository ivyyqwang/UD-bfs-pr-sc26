from EFA_v2 import *
def fcnvt_64_b16_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14429036135264384592]
    tran0.writeAction("movir X16 51262")
    tran0.writeAction("slorii X16 X16 12 958")
    tran0.writeAction("slorii X16 X16 12 2733")
    tran0.writeAction("slorii X16 X16 12 2903")
    tran0.writeAction("slorii X16 X16 12 1616")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
