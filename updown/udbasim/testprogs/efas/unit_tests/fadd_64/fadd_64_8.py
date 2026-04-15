from EFA_v2 import *
def fadd_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13518186587458714407, 2654314482596330309]
    tran0.writeAction("movir X16 48026")
    tran0.writeAction("slorii X16 X16 12 1009")
    tran0.writeAction("slorii X16 X16 12 1072")
    tran0.writeAction("slorii X16 X16 12 3795")
    tran0.writeAction("slorii X16 X16 12 2855")
    tran0.writeAction("movir X17 9430")
    tran0.writeAction("slorii X17 X17 12 79")
    tran0.writeAction("slorii X17 X17 12 1393")
    tran0.writeAction("slorii X17 X17 12 1347")
    tran0.writeAction("slorii X17 X17 12 2885")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
