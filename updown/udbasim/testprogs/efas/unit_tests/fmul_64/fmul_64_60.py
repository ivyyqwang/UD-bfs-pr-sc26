from EFA_v2 import *
def fmul_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1859532961614922293, 3146976994984888141]
    tran0.writeAction("movir X16 6606")
    tran0.writeAction("slorii X16 X16 12 1590")
    tran0.writeAction("slorii X16 X16 12 89")
    tran0.writeAction("slorii X16 X16 12 768")
    tran0.writeAction("slorii X16 X16 12 565")
    tran0.writeAction("movir X17 11180")
    tran0.writeAction("slorii X17 X17 12 1262")
    tran0.writeAction("slorii X17 X17 12 1870")
    tran0.writeAction("slorii X17 X17 12 1640")
    tran0.writeAction("slorii X17 X17 12 1869")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
