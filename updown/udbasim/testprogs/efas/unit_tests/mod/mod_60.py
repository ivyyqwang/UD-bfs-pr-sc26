from EFA_v2 import *
def mod_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4959249386671755557, 1432900248633874778]
    tran0.writeAction("movir X16 17618")
    tran0.writeAction("slorii X16 X16 12 3248")
    tran0.writeAction("slorii X16 X16 12 2749")
    tran0.writeAction("slorii X16 X16 12 589")
    tran0.writeAction("slorii X16 X16 12 293")
    tran0.writeAction("movir X17 5090")
    tran0.writeAction("slorii X17 X17 12 2802")
    tran0.writeAction("slorii X17 X17 12 3886")
    tran0.writeAction("slorii X17 X17 12 1601")
    tran0.writeAction("slorii X17 X17 12 2394")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
