from EFA_v2 import *
def fdiv_64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14289384607335767993, 9513530508568545961]
    tran0.writeAction("movir X16 50766")
    tran0.writeAction("slorii X16 X16 12 377")
    tran0.writeAction("slorii X16 X16 12 1931")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("slorii X16 X16 12 4025")
    tran0.writeAction("movir X17 33798")
    tran0.writeAction("slorii X17 X17 12 3481")
    tran0.writeAction("slorii X17 X17 12 1979")
    tran0.writeAction("slorii X17 X17 12 284")
    tran0.writeAction("slorii X17 X17 12 2729")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
