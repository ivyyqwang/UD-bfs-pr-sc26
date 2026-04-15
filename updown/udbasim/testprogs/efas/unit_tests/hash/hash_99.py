from EFA_v2 import *
def hash_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2929103351426121877, 8797247003115313473]
    tran0.writeAction("movir X16 10406")
    tran0.writeAction("slorii X16 X16 12 1087")
    tran0.writeAction("slorii X16 X16 12 2724")
    tran0.writeAction("slorii X16 X16 12 656")
    tran0.writeAction("slorii X16 X16 12 149")
    tran0.writeAction("movir X17 31254")
    tran0.writeAction("slorii X17 X17 12 408")
    tran0.writeAction("slorii X17 X17 12 2590")
    tran0.writeAction("slorii X17 X17 12 237")
    tran0.writeAction("slorii X17 X17 12 2369")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
