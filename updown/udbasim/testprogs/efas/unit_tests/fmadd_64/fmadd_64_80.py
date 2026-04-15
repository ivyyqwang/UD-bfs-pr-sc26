from EFA_v2 import *
def fmadd_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5000775043912266546, 12132738335595229058, 15157309163408914098]
    tran0.writeAction("movir X16 17766")
    tran0.writeAction("slorii X16 X16 12 1318")
    tran0.writeAction("slorii X16 X16 12 2110")
    tran0.writeAction("slorii X16 X16 12 119")
    tran0.writeAction("slorii X16 X16 12 818")
    tran0.writeAction("movir X17 43104")
    tran0.writeAction("slorii X17 X17 12 595")
    tran0.writeAction("slorii X17 X17 12 3061")
    tran0.writeAction("slorii X17 X17 12 3758")
    tran0.writeAction("slorii X17 X17 12 3970")
    tran0.writeAction("movir X18 53849")
    tran0.writeAction("slorii X18 X18 12 2374")
    tran0.writeAction("slorii X18 X18 12 147")
    tran0.writeAction("slorii X18 X18 12 3119")
    tran0.writeAction("slorii X18 X18 12 1714")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
