from EFA_v2 import *
def fmadd_32_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [469285203, 3898245812, 120472641]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 27")
    tran0.writeAction("slorii X16 X16 12 3979")
    tran0.writeAction("slorii X16 X16 12 2387")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 232")
    tran0.writeAction("slorii X17 X17 12 1448")
    tran0.writeAction("slorii X17 X17 12 692")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 7")
    tran0.writeAction("slorii X18 X18 12 740")
    tran0.writeAction("slorii X18 X18 12 1089")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
