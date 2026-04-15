from EFA_v2 import *
def divi_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7031291554123588052, 15619]
    tran0.writeAction("movir X16 24980")
    tran0.writeAction("slorii X16 X16 12 678")
    tran0.writeAction("slorii X16 X16 12 2627")
    tran0.writeAction("slorii X16 X16 12 3034")
    tran0.writeAction("slorii X16 X16 12 468")
    tran0.writeAction("divi X16 X17 15619")
    tran0.writeAction("yieldt")
    return efa
