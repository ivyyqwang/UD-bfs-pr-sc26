from EFA_v2 import *
def divi_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1013680042575900593, -1001]
    tran0.writeAction("movir X16 3601")
    tran0.writeAction("slorii X16 X16 12 1290")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("slorii X16 X16 12 2618")
    tran0.writeAction("slorii X16 X16 12 4017")
    tran0.writeAction("divi X16 X17 -1001")
    tran0.writeAction("yieldt")
    return efa
