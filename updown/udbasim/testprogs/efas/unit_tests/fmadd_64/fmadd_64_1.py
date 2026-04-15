from EFA_v2 import *
def fmadd_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17568604000407378927, 1920452032538209377, 6518609164396852118]
    tran0.writeAction("movir X16 62416")
    tran0.writeAction("slorii X16 X16 12 900")
    tran0.writeAction("slorii X16 X16 12 387")
    tran0.writeAction("slorii X16 X16 12 3229")
    tran0.writeAction("slorii X16 X16 12 3055")
    tran0.writeAction("movir X17 6822")
    tran0.writeAction("slorii X17 X17 12 3343")
    tran0.writeAction("slorii X17 X17 12 727")
    tran0.writeAction("slorii X17 X17 12 2526")
    tran0.writeAction("slorii X17 X17 12 3169")
    tran0.writeAction("movir X18 23158")
    tran0.writeAction("slorii X18 X18 12 3079")
    tran0.writeAction("slorii X18 X18 12 3961")
    tran0.writeAction("slorii X18 X18 12 1967")
    tran0.writeAction("slorii X18 X18 12 918")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
