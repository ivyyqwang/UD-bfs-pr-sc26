from EFA_v2 import *
def fmadd_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9568300731671123352, 6659389725934106430, 1064728440033216679]
    tran0.writeAction("movir X16 33993")
    tran0.writeAction("slorii X16 X16 12 1773")
    tran0.writeAction("slorii X16 X16 12 519")
    tran0.writeAction("slorii X16 X16 12 1505")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("movir X17 23658")
    tran0.writeAction("slorii X17 X17 12 3706")
    tran0.writeAction("slorii X17 X17 12 3131")
    tran0.writeAction("slorii X17 X17 12 771")
    tran0.writeAction("slorii X17 X17 12 1854")
    tran0.writeAction("movir X18 3782")
    tran0.writeAction("slorii X18 X18 12 2766")
    tran0.writeAction("slorii X18 X18 12 2")
    tran0.writeAction("slorii X18 X18 12 1784")
    tran0.writeAction("slorii X18 X18 12 2215")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
