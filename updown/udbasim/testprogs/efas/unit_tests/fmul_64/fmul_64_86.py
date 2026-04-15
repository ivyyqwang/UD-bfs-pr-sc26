from EFA_v2 import *
def fmul_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12297547860836925599, 14532969256630217513]
    tran0.writeAction("movir X16 43689")
    tran0.writeAction("slorii X16 X16 12 2729")
    tran0.writeAction("slorii X16 X16 12 4045")
    tran0.writeAction("slorii X16 X16 12 2252")
    tran0.writeAction("slorii X16 X16 12 159")
    tran0.writeAction("movir X17 51631")
    tran0.writeAction("slorii X17 X17 12 1960")
    tran0.writeAction("slorii X17 X17 12 2617")
    tran0.writeAction("slorii X17 X17 12 478")
    tran0.writeAction("slorii X17 X17 12 2857")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
