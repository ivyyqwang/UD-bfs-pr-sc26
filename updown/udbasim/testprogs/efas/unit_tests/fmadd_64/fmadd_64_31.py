from EFA_v2 import *
def fmadd_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11884521835009154513, 14919220267631109325, 3839209265984550888]
    tran0.writeAction("movir X16 42222")
    tran0.writeAction("slorii X16 X16 12 1242")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("slorii X16 X16 12 385")
    tran0.writeAction("slorii X16 X16 12 3537")
    tran0.writeAction("movir X17 53003")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("slorii X17 X17 12 2489")
    tran0.writeAction("slorii X17 X17 12 3934")
    tran0.writeAction("slorii X17 X17 12 1229")
    tran0.writeAction("movir X18 13639")
    tran0.writeAction("slorii X18 X18 12 2503")
    tran0.writeAction("slorii X18 X18 12 3205")
    tran0.writeAction("slorii X18 X18 12 1627")
    tran0.writeAction("slorii X18 X18 12 2024")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
