from EFA_v2 import *
def fmadd_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16127902198596592333, 1735687252933273770, 5457054968685307057]
    tran0.writeAction("movir X16 57297")
    tran0.writeAction("slorii X16 X16 12 3353")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 2422")
    tran0.writeAction("slorii X16 X16 12 717")
    tran0.writeAction("movir X17 6166")
    tran0.writeAction("slorii X17 X17 12 1637")
    tran0.writeAction("slorii X17 X17 12 3144")
    tran0.writeAction("slorii X17 X17 12 1070")
    tran0.writeAction("slorii X17 X17 12 2218")
    tran0.writeAction("movir X18 19387")
    tran0.writeAction("slorii X18 X18 12 1449")
    tran0.writeAction("slorii X18 X18 12 1232")
    tran0.writeAction("slorii X18 X18 12 1098")
    tran0.writeAction("slorii X18 X18 12 1201")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
