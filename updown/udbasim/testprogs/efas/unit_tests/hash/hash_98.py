from EFA_v2 import *
def hash_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7693763109215958328, 8567801398495880206]
    tran0.writeAction("movir X16 38202")
    tran0.writeAction("slorii X16 X16 12 1075")
    tran0.writeAction("slorii X16 X16 12 1833")
    tran0.writeAction("slorii X16 X16 12 728")
    tran0.writeAction("slorii X16 X16 12 2760")
    tran0.writeAction("movir X17 30438")
    tran0.writeAction("slorii X17 X17 12 3871")
    tran0.writeAction("slorii X17 X17 12 2639")
    tran0.writeAction("slorii X17 X17 12 1810")
    tran0.writeAction("slorii X17 X17 12 1038")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
