from EFA_v2 import *
def fsub_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9476273525476494750, 10037836061637546131]
    tran0.writeAction("movir X16 33666")
    tran0.writeAction("slorii X16 X16 12 1993")
    tran0.writeAction("slorii X16 X16 12 96")
    tran0.writeAction("slorii X16 X16 12 1904")
    tran0.writeAction("slorii X16 X16 12 3486")
    tran0.writeAction("movir X17 35661")
    tran0.writeAction("slorii X17 X17 12 2283")
    tran0.writeAction("slorii X17 X17 12 1823")
    tran0.writeAction("slorii X17 X17 12 2097")
    tran0.writeAction("slorii X17 X17 12 147")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
