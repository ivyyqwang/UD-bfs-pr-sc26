from EFA_v2 import *
def fmul_64_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17218639325325273340, 6855704224080816789]
    tran0.writeAction("movir X16 61172")
    tran0.writeAction("slorii X16 X16 12 3667")
    tran0.writeAction("slorii X16 X16 12 3317")
    tran0.writeAction("slorii X16 X16 12 2394")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("movir X17 24356")
    tran0.writeAction("slorii X17 X17 12 1450")
    tran0.writeAction("slorii X17 X17 12 2865")
    tran0.writeAction("slorii X17 X17 12 1974")
    tran0.writeAction("slorii X17 X17 12 2709")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
