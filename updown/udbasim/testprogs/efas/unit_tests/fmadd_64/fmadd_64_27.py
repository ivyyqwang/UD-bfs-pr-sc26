from EFA_v2 import *
def fmadd_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [271691055038616664, 16634840535576683120, 7251040076108521943]
    tran0.writeAction("movir X16 965")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("slorii X16 X16 12 824")
    tran0.writeAction("slorii X16 X16 12 933")
    tran0.writeAction("slorii X16 X16 12 1112")
    tran0.writeAction("movir X17 59098")
    tran0.writeAction("slorii X17 X17 12 3381")
    tran0.writeAction("slorii X17 X17 12 1274")
    tran0.writeAction("slorii X17 X17 12 1298")
    tran0.writeAction("slorii X17 X17 12 624")
    tran0.writeAction("movir X18 25760")
    tran0.writeAction("slorii X18 X18 12 3560")
    tran0.writeAction("slorii X18 X18 12 2068")
    tran0.writeAction("slorii X18 X18 12 2334")
    tran0.writeAction("slorii X18 X18 12 471")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
