from EFA_v2 import *
def fmadd_64_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18081915398679436825, 18415770057611914172, 12821120312017630146]
    tran0.writeAction("movir X16 64239")
    tran0.writeAction("slorii X16 X16 12 3556")
    tran0.writeAction("slorii X16 X16 12 196")
    tran0.writeAction("slorii X16 X16 12 3905")
    tran0.writeAction("slorii X16 X16 12 3609")
    tran0.writeAction("movir X17 65425")
    tran0.writeAction("slorii X17 X17 12 3924")
    tran0.writeAction("slorii X17 X17 12 3045")
    tran0.writeAction("slorii X17 X17 12 954")
    tran0.writeAction("slorii X17 X17 12 3004")
    tran0.writeAction("movir X18 45549")
    tran0.writeAction("slorii X18 X18 12 3151")
    tran0.writeAction("slorii X18 X18 12 3740")
    tran0.writeAction("slorii X18 X18 12 1459")
    tran0.writeAction("slorii X18 X18 12 962")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
