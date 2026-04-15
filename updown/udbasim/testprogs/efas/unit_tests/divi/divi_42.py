from EFA_v2 import *
def divi_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3725534577210193511, 3377]
    tran0.writeAction("movir X16 52300")
    tran0.writeAction("slorii X16 X16 12 992")
    tran0.writeAction("slorii X16 X16 12 2670")
    tran0.writeAction("slorii X16 X16 12 3896")
    tran0.writeAction("slorii X16 X16 12 2457")
    tran0.writeAction("divi X16 X17 3377")
    tran0.writeAction("yieldt")
    return efa
