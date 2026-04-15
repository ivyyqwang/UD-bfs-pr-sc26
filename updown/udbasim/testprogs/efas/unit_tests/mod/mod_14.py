from EFA_v2 import *
def mod_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-587480730799466288, -3950622704841538045]
    tran0.writeAction("movir X16 63448")
    tran0.writeAction("slorii X16 X16 12 3478")
    tran0.writeAction("slorii X16 X16 12 848")
    tran0.writeAction("slorii X16 X16 12 1273")
    tran0.writeAction("slorii X16 X16 12 2256")
    tran0.writeAction("movir X17 51500")
    tran0.writeAction("slorii X17 X17 12 2329")
    tran0.writeAction("slorii X17 X17 12 1228")
    tran0.writeAction("slorii X17 X17 12 1340")
    tran0.writeAction("slorii X17 X17 12 1539")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
