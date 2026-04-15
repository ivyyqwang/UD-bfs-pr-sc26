from EFA_v2 import *
def fadd_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1266504079887577095, 9988431142249745990]
    tran0.writeAction("movir X16 4499")
    tran0.writeAction("slorii X16 X16 12 2156")
    tran0.writeAction("slorii X16 X16 12 28")
    tran0.writeAction("slorii X16 X16 12 1155")
    tran0.writeAction("slorii X16 X16 12 7")
    tran0.writeAction("movir X17 35486")
    tran0.writeAction("slorii X17 X17 12 147")
    tran0.writeAction("slorii X17 X17 12 1009")
    tran0.writeAction("slorii X17 X17 12 1004")
    tran0.writeAction("slorii X17 X17 12 3654")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
