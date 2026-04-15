from EFA_v2 import *
def hash_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4065629981735286584, 1649609174570310699]
    tran0.writeAction("movir X16 14444")
    tran0.writeAction("slorii X16 X16 12 78")
    tran0.writeAction("slorii X16 X16 12 3457")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("slorii X16 X16 12 1848")
    tran0.writeAction("movir X17 5860")
    tran0.writeAction("slorii X17 X17 12 2412")
    tran0.writeAction("slorii X17 X17 12 3556")
    tran0.writeAction("slorii X17 X17 12 2001")
    tran0.writeAction("slorii X17 X17 12 3115")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
