from EFA_v2 import *
def fmadd_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8826378421623638458, 16132013072570072080, 13124843835301292991]
    tran0.writeAction("movir X16 31357")
    tran0.writeAction("slorii X16 X16 12 2438")
    tran0.writeAction("slorii X16 X16 12 2314")
    tran0.writeAction("slorii X16 X16 12 204")
    tran0.writeAction("slorii X16 X16 12 2490")
    tran0.writeAction("movir X17 57312")
    tran0.writeAction("slorii X17 X17 12 1734")
    tran0.writeAction("slorii X17 X17 12 2846")
    tran0.writeAction("slorii X17 X17 12 2035")
    tran0.writeAction("slorii X17 X17 12 3088")
    tran0.writeAction("movir X18 46628")
    tran0.writeAction("slorii X18 X18 12 3326")
    tran0.writeAction("slorii X18 X18 12 3591")
    tran0.writeAction("slorii X18 X18 12 2494")
    tran0.writeAction("slorii X18 X18 12 3007")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
