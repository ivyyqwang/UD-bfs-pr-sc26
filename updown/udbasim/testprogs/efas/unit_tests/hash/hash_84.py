from EFA_v2 import *
def hash_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1351640360498834512, 6228623779414949569]
    tran0.writeAction("movir X16 4801")
    tran0.writeAction("slorii X16 X16 12 4059")
    tran0.writeAction("slorii X16 X16 12 3871")
    tran0.writeAction("slorii X16 X16 12 2514")
    tran0.writeAction("slorii X16 X16 12 3152")
    tran0.writeAction("movir X17 22128")
    tran0.writeAction("slorii X17 X17 12 2117")
    tran0.writeAction("slorii X17 X17 12 931")
    tran0.writeAction("slorii X17 X17 12 2371")
    tran0.writeAction("slorii X17 X17 12 3777")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
