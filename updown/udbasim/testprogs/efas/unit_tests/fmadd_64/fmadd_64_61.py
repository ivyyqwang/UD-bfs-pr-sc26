from EFA_v2 import *
def fmadd_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10131880903726495837, 11426047024659993435, 3833814533566537960]
    tran0.writeAction("movir X16 35995")
    tran0.writeAction("slorii X16 X16 12 2752")
    tran0.writeAction("slorii X16 X16 12 61")
    tran0.writeAction("slorii X16 X16 12 743")
    tran0.writeAction("slorii X16 X16 12 2141")
    tran0.writeAction("movir X17 40593")
    tran0.writeAction("slorii X17 X17 12 1939")
    tran0.writeAction("slorii X17 X17 12 2859")
    tran0.writeAction("slorii X17 X17 12 3145")
    tran0.writeAction("slorii X17 X17 12 859")
    tran0.writeAction("movir X18 13620")
    tran0.writeAction("slorii X18 X18 12 1824")
    tran0.writeAction("slorii X18 X18 12 383")
    tran0.writeAction("slorii X18 X18 12 3946")
    tran0.writeAction("slorii X18 X18 12 232")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
