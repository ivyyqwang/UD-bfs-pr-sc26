from EFA_v2 import *
def fcnvt_64_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10463074948022664246]
    tran0.writeAction("movir X16 37172")
    tran0.writeAction("slorii X16 X16 12 1267")
    tran0.writeAction("slorii X16 X16 12 2751")
    tran0.writeAction("slorii X16 X16 12 735")
    tran0.writeAction("slorii X16 X16 12 3126")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
