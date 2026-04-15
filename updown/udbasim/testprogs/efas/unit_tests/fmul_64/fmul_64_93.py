from EFA_v2 import *
def fmul_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7344230623367033766, 969237855051142906]
    tran0.writeAction("movir X16 26091")
    tran0.writeAction("slorii X16 X16 12 3885")
    tran0.writeAction("slorii X16 X16 12 1838")
    tran0.writeAction("slorii X16 X16 12 1383")
    tran0.writeAction("slorii X16 X16 12 934")
    tran0.writeAction("movir X17 3443")
    tran0.writeAction("slorii X17 X17 12 1739")
    tran0.writeAction("slorii X17 X17 12 421")
    tran0.writeAction("slorii X17 X17 12 757")
    tran0.writeAction("slorii X17 X17 12 1786")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
