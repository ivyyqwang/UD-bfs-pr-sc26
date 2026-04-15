from EFA_v2 import *
def fdiv_64_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11966381601464900236, 2817844486464596521]
    tran0.writeAction("movir X16 42513")
    tran0.writeAction("slorii X16 X16 12 522")
    tran0.writeAction("slorii X16 X16 12 2682")
    tran0.writeAction("slorii X16 X16 12 349")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("movir X17 10010")
    tran0.writeAction("slorii X17 X17 12 4074")
    tran0.writeAction("slorii X17 X17 12 384")
    tran0.writeAction("slorii X17 X17 12 62")
    tran0.writeAction("slorii X17 X17 12 2601")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
