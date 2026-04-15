from EFA_v2 import *
def fdiv_64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3957673783687537965, 15852204265503060424]
    tran0.writeAction("movir X16 14060")
    tran0.writeAction("slorii X16 X16 12 1973")
    tran0.writeAction("slorii X16 X16 12 1645")
    tran0.writeAction("slorii X16 X16 12 2342")
    tran0.writeAction("slorii X16 X16 12 1325")
    tran0.writeAction("movir X17 56318")
    tran0.writeAction("slorii X17 X17 12 1404")
    tran0.writeAction("slorii X17 X17 12 2680")
    tran0.writeAction("slorii X17 X17 12 991")
    tran0.writeAction("slorii X17 X17 12 456")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
