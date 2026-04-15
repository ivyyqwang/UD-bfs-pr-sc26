from EFA_v2 import *
def fmul_64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7992656388181133192, 16130368968435492921]
    tran0.writeAction("movir X16 28395")
    tran0.writeAction("slorii X16 X16 12 2538")
    tran0.writeAction("slorii X16 X16 12 861")
    tran0.writeAction("slorii X16 X16 12 1200")
    tran0.writeAction("slorii X16 X16 12 1928")
    tran0.writeAction("movir X17 57306")
    tran0.writeAction("slorii X17 X17 12 2385")
    tran0.writeAction("slorii X17 X17 12 3403")
    tran0.writeAction("slorii X17 X17 12 2382")
    tran0.writeAction("slorii X17 X17 12 2105")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
