from EFA_v2 import *
def hash_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3921714081758479988, 5605384966591317715]
    tran0.writeAction("movir X16 51603")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("slorii X16 X16 12 542")
    tran0.writeAction("slorii X16 X16 12 567")
    tran0.writeAction("slorii X16 X16 12 2444")
    tran0.writeAction("movir X17 19914")
    tran0.writeAction("slorii X17 X17 12 1342")
    tran0.writeAction("slorii X17 X17 12 3506")
    tran0.writeAction("slorii X17 X17 12 4056")
    tran0.writeAction("slorii X17 X17 12 1747")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
