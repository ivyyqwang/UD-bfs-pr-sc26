from EFA_v2 import *
def add_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [462282099111840361, -3193397647765616750]
    tran0.writeAction("movir X16 1642")
    tran0.writeAction("slorii X16 X16 12 1457")
    tran0.writeAction("slorii X16 X16 12 3759")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("slorii X16 X16 12 2665")
    tran0.writeAction("movir X17 54190")
    tran0.writeAction("slorii X17 X17 12 3164")
    tran0.writeAction("slorii X17 X17 12 570")
    tran0.writeAction("slorii X17 X17 12 1484")
    tran0.writeAction("slorii X17 X17 12 1938")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
