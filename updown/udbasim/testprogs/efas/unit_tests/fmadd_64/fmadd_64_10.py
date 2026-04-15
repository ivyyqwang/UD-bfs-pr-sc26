from EFA_v2 import *
def fmadd_64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9603353188578127892, 10895578860929759825, 15929077954877391570]
    tran0.writeAction("movir X16 34117")
    tran0.writeAction("slorii X16 X16 12 3949")
    tran0.writeAction("slorii X16 X16 12 2081")
    tran0.writeAction("slorii X16 X16 12 3335")
    tran0.writeAction("slorii X16 X16 12 20")
    tran0.writeAction("movir X17 38708")
    tran0.writeAction("slorii X17 X17 12 3571")
    tran0.writeAction("slorii X17 X17 12 3883")
    tran0.writeAction("slorii X17 X17 12 3987")
    tran0.writeAction("slorii X17 X17 12 2641")
    tran0.writeAction("movir X18 56591")
    tran0.writeAction("slorii X18 X18 12 1856")
    tran0.writeAction("slorii X18 X18 12 267")
    tran0.writeAction("slorii X18 X18 12 3984")
    tran0.writeAction("slorii X18 X18 12 722")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
