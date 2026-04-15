from EFA_v2 import *
def fmadd_64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [167127561869305001, 13162166378011769250, 18416359987478985481]
    tran0.writeAction("movir X16 593")
    tran0.writeAction("slorii X16 X16 12 3098")
    tran0.writeAction("slorii X16 X16 12 461")
    tran0.writeAction("slorii X16 X16 12 1626")
    tran0.writeAction("slorii X16 X16 12 1193")
    tran0.writeAction("movir X17 46761")
    tran0.writeAction("slorii X17 X17 12 1673")
    tran0.writeAction("slorii X17 X17 12 1451")
    tran0.writeAction("slorii X17 X17 12 4019")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("movir X18 65428")
    tran0.writeAction("slorii X18 X18 12 221")
    tran0.writeAction("slorii X18 X18 12 1445")
    tran0.writeAction("slorii X18 X18 12 1647")
    tran0.writeAction("slorii X18 X18 12 2825")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
