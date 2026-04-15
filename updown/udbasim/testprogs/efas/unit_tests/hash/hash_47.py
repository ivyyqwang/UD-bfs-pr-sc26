from EFA_v2 import *
def hash_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3726440740070123740, 2405167985286709163]
    tran0.writeAction("movir X16 52297")
    tran0.writeAction("slorii X16 X16 12 94")
    tran0.writeAction("slorii X16 X16 12 1011")
    tran0.writeAction("slorii X16 X16 12 2361")
    tran0.writeAction("slorii X16 X16 12 1828")
    tran0.writeAction("movir X17 8544")
    tran0.writeAction("slorii X17 X17 12 3576")
    tran0.writeAction("slorii X17 X17 12 2588")
    tran0.writeAction("slorii X17 X17 12 639")
    tran0.writeAction("slorii X17 X17 12 4011")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
