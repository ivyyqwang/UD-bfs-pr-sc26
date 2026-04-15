from EFA_v2 import *
def divi_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3076344898108027189, 28085]
    tran0.writeAction("movir X16 54606")
    tran0.writeAction("slorii X16 X16 12 2569")
    tran0.writeAction("slorii X16 X16 12 3397")
    tran0.writeAction("slorii X16 X16 12 2808")
    tran0.writeAction("slorii X16 X16 12 3787")
    tran0.writeAction("divi X16 X17 28085")
    tran0.writeAction("yieldt")
    return efa
