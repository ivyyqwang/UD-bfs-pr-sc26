from EFA_v2 import *
def fdiv_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3492306784890044612, 13708899037851656164]
    tran0.writeAction("movir X16 12407")
    tran0.writeAction("slorii X16 X16 12 680")
    tran0.writeAction("slorii X16 X16 12 1168")
    tran0.writeAction("slorii X16 X16 12 236")
    tran0.writeAction("slorii X16 X16 12 196")
    tran0.writeAction("movir X17 48703")
    tran0.writeAction("slorii X17 X17 12 3248")
    tran0.writeAction("slorii X17 X17 12 2756")
    tran0.writeAction("slorii X17 X17 12 3449")
    tran0.writeAction("slorii X17 X17 12 4068")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
