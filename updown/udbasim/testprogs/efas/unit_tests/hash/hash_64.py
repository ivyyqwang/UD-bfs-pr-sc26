from EFA_v2 import *
def hash_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3125885867631777439, -756780977378805957]
    tran0.writeAction("movir X16 11105")
    tran0.writeAction("slorii X16 X16 12 1546")
    tran0.writeAction("slorii X16 X16 12 652")
    tran0.writeAction("slorii X16 X16 12 2481")
    tran0.writeAction("slorii X16 X16 12 1695")
    tran0.writeAction("movir X17 62847")
    tran0.writeAction("slorii X17 X17 12 1531")
    tran0.writeAction("slorii X17 X17 12 1518")
    tran0.writeAction("slorii X17 X17 12 2307")
    tran0.writeAction("slorii X17 X17 12 1851")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
