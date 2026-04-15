from EFA_v2 import *
def fmul_32_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [746936976, 3542447640]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 44")
    tran0.writeAction("slorii X16 X16 12 2133")
    tran0.writeAction("slorii X16 X16 12 2704")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 211")
    tran0.writeAction("slorii X17 X17 12 599")
    tran0.writeAction("slorii X17 X17 12 1560")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
