from EFA_v2 import *
def fadd_64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17935794768563595258, 3342580783556340746]
    tran0.writeAction("movir X16 63720")
    tran0.writeAction("slorii X16 X16 12 3045")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("slorii X16 X16 12 2222")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("movir X17 11875")
    tran0.writeAction("slorii X17 X17 12 952")
    tran0.writeAction("slorii X17 X17 12 844")
    tran0.writeAction("slorii X17 X17 12 3778")
    tran0.writeAction("slorii X17 X17 12 3082")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
