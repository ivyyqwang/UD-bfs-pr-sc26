from EFA_v2 import *
def hash_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5765880479822192587, 5762161889579736329]
    tran0.writeAction("movir X16 20484")
    tran0.writeAction("slorii X16 X16 12 2139")
    tran0.writeAction("slorii X16 X16 12 3929")
    tran0.writeAction("slorii X16 X16 12 657")
    tran0.writeAction("slorii X16 X16 12 4043")
    tran0.writeAction("movir X17 20471")
    tran0.writeAction("slorii X17 X17 12 1275")
    tran0.writeAction("slorii X17 X17 12 1430")
    tran0.writeAction("slorii X17 X17 12 2841")
    tran0.writeAction("slorii X17 X17 12 3337")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
