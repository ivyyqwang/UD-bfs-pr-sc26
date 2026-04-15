from EFA_v2 import *
def fmadd_32_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2774294707, 2382584467, 1871673625]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("slorii X16 X16 12 1478")
    tran0.writeAction("slorii X16 X16 12 179")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 142")
    tran0.writeAction("slorii X17 X17 12 53")
    tran0.writeAction("slorii X17 X17 12 2707")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 111")
    tran0.writeAction("slorii X18 X18 12 2295")
    tran0.writeAction("slorii X18 X18 12 2329")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
