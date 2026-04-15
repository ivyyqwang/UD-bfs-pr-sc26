from EFA_v2 import *
def fmadd_64_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12589942408919407703, 4567094414543734832, 6810546589718559396]
    tran0.writeAction("movir X16 44728")
    tran0.writeAction("slorii X16 X16 12 1886")
    tran0.writeAction("slorii X16 X16 12 2722")
    tran0.writeAction("slorii X16 X16 12 1093")
    tran0.writeAction("slorii X16 X16 12 3159")
    tran0.writeAction("movir X17 16225")
    tran0.writeAction("slorii X17 X17 12 2370")
    tran0.writeAction("slorii X17 X17 12 3114")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 12 2096")
    tran0.writeAction("movir X18 24195")
    tran0.writeAction("slorii X18 X18 12 3776")
    tran0.writeAction("slorii X18 X18 12 2590")
    tran0.writeAction("slorii X18 X18 12 1731")
    tran0.writeAction("slorii X18 X18 12 2724")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
