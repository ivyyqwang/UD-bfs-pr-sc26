from EFA_v2 import *
def hash_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3762797377632908589, -7492158634123894016]
    tran0.writeAction("movir X16 52167")
    tran0.writeAction("slorii X16 X16 12 3515")
    tran0.writeAction("slorii X16 X16 12 2208")
    tran0.writeAction("slorii X16 X16 12 1716")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("movir X17 38918")
    tran0.writeAction("slorii X17 X17 12 2070")
    tran0.writeAction("slorii X17 X17 12 2780")
    tran0.writeAction("slorii X17 X17 12 694")
    tran0.writeAction("slorii X17 X17 12 768")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
