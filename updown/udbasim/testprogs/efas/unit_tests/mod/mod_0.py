from EFA_v2 import *
def mod_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3622825647016829298, 3068208684215398657]
    tran0.writeAction("movir X16 52665")
    tran0.writeAction("slorii X16 X16 12 564")
    tran0.writeAction("slorii X16 X16 12 1218")
    tran0.writeAction("slorii X16 X16 12 1585")
    tran0.writeAction("slorii X16 X16 12 3726")
    tran0.writeAction("movir X17 10900")
    tran0.writeAction("slorii X17 X17 12 1912")
    tran0.writeAction("slorii X17 X17 12 2767")
    tran0.writeAction("slorii X17 X17 12 1751")
    tran0.writeAction("slorii X17 X17 12 257")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
