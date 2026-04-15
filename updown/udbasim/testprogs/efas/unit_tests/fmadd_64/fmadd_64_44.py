from EFA_v2 import *
def fmadd_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [582194296441387374, 1417845674833483852, 5145041375474787825]
    tran0.writeAction("movir X16 2068")
    tran0.writeAction("slorii X16 X16 12 1514")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("slorii X16 X16 12 2651")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("movir X17 5037")
    tran0.writeAction("slorii X17 X17 12 818")
    tran0.writeAction("slorii X17 X17 12 274")
    tran0.writeAction("slorii X17 X17 12 3169")
    tran0.writeAction("slorii X17 X17 12 2124")
    tran0.writeAction("movir X18 18278")
    tran0.writeAction("slorii X18 X18 12 3517")
    tran0.writeAction("slorii X18 X18 12 3859")
    tran0.writeAction("slorii X18 X18 12 3530")
    tran0.writeAction("slorii X18 X18 12 1521")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
