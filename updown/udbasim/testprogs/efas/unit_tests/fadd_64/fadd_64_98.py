from EFA_v2 import *
def fadd_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3047820800074659125, 2024174232822614026]
    tran0.writeAction("movir X16 10828")
    tran0.writeAction("slorii X16 X16 12 141")
    tran0.writeAction("slorii X16 X16 12 3743")
    tran0.writeAction("slorii X16 X16 12 2035")
    tran0.writeAction("slorii X16 X16 12 1333")
    tran0.writeAction("movir X17 7191")
    tran0.writeAction("slorii X17 X17 12 1275")
    tran0.writeAction("slorii X17 X17 12 3454")
    tran0.writeAction("slorii X17 X17 12 3648")
    tran0.writeAction("slorii X17 X17 12 2058")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
