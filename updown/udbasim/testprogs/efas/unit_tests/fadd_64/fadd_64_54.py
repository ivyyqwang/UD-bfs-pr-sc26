from EFA_v2 import *
def fadd_64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4910234677577531738, 9958107386547807258]
    tran0.writeAction("movir X16 17444")
    tran0.writeAction("slorii X16 X16 12 2694")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 3332")
    tran0.writeAction("slorii X16 X16 12 346")
    tran0.writeAction("movir X17 35378")
    tran0.writeAction("slorii X17 X17 12 1246")
    tran0.writeAction("slorii X17 X17 12 2146")
    tran0.writeAction("slorii X17 X17 12 1538")
    tran0.writeAction("slorii X17 X17 12 1050")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
