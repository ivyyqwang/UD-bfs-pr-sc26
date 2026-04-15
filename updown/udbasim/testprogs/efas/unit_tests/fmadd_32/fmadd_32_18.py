from EFA_v2 import *
def fmadd_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1600108028, 2651033439, 1405559840]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 95")
    tran0.writeAction("slorii X16 X16 12 1531")
    tran0.writeAction("slorii X16 X16 12 1532")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 158")
    tran0.writeAction("slorii X17 X17 12 56")
    tran0.writeAction("slorii X17 X17 12 3935")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 83")
    tran0.writeAction("slorii X18 X18 12 3186")
    tran0.writeAction("slorii X18 X18 12 1056")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
