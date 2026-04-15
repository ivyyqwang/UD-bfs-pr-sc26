from EFA_v2 import *
def fmul_32_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4147819348, 2494958256]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("slorii X16 X16 12 939")
    tran0.writeAction("slorii X16 X16 12 852")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 148")
    tran0.writeAction("slorii X17 X17 12 2912")
    tran0.writeAction("slorii X17 X17 12 2736")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
