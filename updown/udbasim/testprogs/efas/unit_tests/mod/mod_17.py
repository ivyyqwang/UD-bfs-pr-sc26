from EFA_v2 import *
def mod_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5512622030536749753, -2234107926905210435]
    tran0.writeAction("movir X16 45951")
    tran0.writeAction("slorii X16 X16 12 951")
    tran0.writeAction("slorii X16 X16 12 2152")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("slorii X16 X16 12 3399")
    tran0.writeAction("movir X17 57598")
    tran0.writeAction("slorii X17 X17 12 3498")
    tran0.writeAction("slorii X17 X17 12 3426")
    tran0.writeAction("slorii X17 X17 12 3811")
    tran0.writeAction("slorii X17 X17 12 2493")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
