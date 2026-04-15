from EFA_v2 import *
def fmadd_64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7482487377670085983, 17720597403317092740, 16077820281310195706]
    tran0.writeAction("movir X16 26583")
    tran0.writeAction("slorii X16 X16 12 554")
    tran0.writeAction("slorii X16 X16 12 70")
    tran0.writeAction("slorii X16 X16 12 1513")
    tran0.writeAction("slorii X16 X16 12 3423")
    tran0.writeAction("movir X17 62956")
    tran0.writeAction("slorii X17 X17 12 855")
    tran0.writeAction("slorii X17 X17 12 856")
    tran0.writeAction("slorii X17 X17 12 1740")
    tran0.writeAction("slorii X17 X17 12 388")
    tran0.writeAction("movir X18 57119")
    tran0.writeAction("slorii X18 X18 12 3653")
    tran0.writeAction("slorii X18 X18 12 3238")
    tran0.writeAction("slorii X18 X18 12 266")
    tran0.writeAction("slorii X18 X18 12 4090")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
