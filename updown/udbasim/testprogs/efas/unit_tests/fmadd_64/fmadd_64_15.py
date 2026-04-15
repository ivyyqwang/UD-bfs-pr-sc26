from EFA_v2 import *
def fmadd_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16913239622050572730, 7431571815756820815, 18359989857201157527]
    tran0.writeAction("movir X16 60087")
    tran0.writeAction("slorii X16 X16 12 3677")
    tran0.writeAction("slorii X16 X16 12 889")
    tran0.writeAction("slorii X16 X16 12 1582")
    tran0.writeAction("slorii X16 X16 12 2490")
    tran0.writeAction("movir X17 26402")
    tran0.writeAction("slorii X17 X17 12 1011")
    tran0.writeAction("slorii X17 X17 12 312")
    tran0.writeAction("slorii X17 X17 12 4055")
    tran0.writeAction("slorii X17 X17 12 335")
    tran0.writeAction("movir X18 65227")
    tran0.writeAction("slorii X18 X18 12 3223")
    tran0.writeAction("slorii X18 X18 12 4078")
    tran0.writeAction("slorii X18 X18 12 1023")
    tran0.writeAction("slorii X18 X18 12 1431")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
