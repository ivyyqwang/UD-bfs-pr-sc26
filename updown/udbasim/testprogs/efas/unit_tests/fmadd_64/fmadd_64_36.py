from EFA_v2 import *
def fmadd_64_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2881127654928825205, 580056725900231921, 4055509790155851504]
    tran0.writeAction("movir X16 10235")
    tran0.writeAction("slorii X16 X16 12 3365")
    tran0.writeAction("slorii X16 X16 12 1624")
    tran0.writeAction("slorii X16 X16 12 2403")
    tran0.writeAction("slorii X16 X16 12 2933")
    tran0.writeAction("movir X17 2060")
    tran0.writeAction("slorii X17 X17 12 3176")
    tran0.writeAction("slorii X17 X17 12 1240")
    tran0.writeAction("slorii X17 X17 12 3520")
    tran0.writeAction("slorii X17 X17 12 1265")
    tran0.writeAction("movir X18 14408")
    tran0.writeAction("slorii X18 X18 12 266")
    tran0.writeAction("slorii X18 X18 12 2761")
    tran0.writeAction("slorii X18 X18 12 1468")
    tran0.writeAction("slorii X18 X18 12 1776")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
