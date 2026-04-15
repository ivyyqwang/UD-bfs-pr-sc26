from EFA_v2 import *
def fadd_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12138480746970492861, 3214417540237808402]
    tran0.writeAction("movir X16 43124")
    tran0.writeAction("slorii X16 X16 12 2238")
    tran0.writeAction("slorii X16 X16 12 3404")
    tran0.writeAction("slorii X16 X16 12 386")
    tran0.writeAction("slorii X16 X16 12 4029")
    tran0.writeAction("movir X17 11419")
    tran0.writeAction("slorii X17 X17 12 3707")
    tran0.writeAction("slorii X17 X17 12 2269")
    tran0.writeAction("slorii X17 X17 12 2701")
    tran0.writeAction("slorii X17 X17 12 786")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
