from EFA_v2 import *
def hash_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7020007661977990863, 3722065185674352694]
    tran0.writeAction("movir X16 24940")
    tran0.writeAction("slorii X16 X16 12 316")
    tran0.writeAction("slorii X16 X16 12 1636")
    tran0.writeAction("slorii X16 X16 12 2943")
    tran0.writeAction("slorii X16 X16 12 1743")
    tran0.writeAction("movir X17 13223")
    tran0.writeAction("slorii X17 X17 12 1769")
    tran0.writeAction("slorii X17 X17 12 230")
    tran0.writeAction("slorii X17 X17 12 3965")
    tran0.writeAction("slorii X17 X17 12 2102")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
