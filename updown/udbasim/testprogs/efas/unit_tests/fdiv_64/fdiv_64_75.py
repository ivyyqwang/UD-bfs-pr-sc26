from EFA_v2 import *
def fdiv_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10167852272193032311, 16834305014067426221]
    tran0.writeAction("movir X16 36123")
    tran0.writeAction("slorii X16 X16 12 1916")
    tran0.writeAction("slorii X16 X16 12 1308")
    tran0.writeAction("slorii X16 X16 12 2925")
    tran0.writeAction("slorii X16 X16 12 119")
    tran0.writeAction("movir X17 59807")
    tran0.writeAction("slorii X17 X17 12 1907")
    tran0.writeAction("slorii X17 X17 12 2020")
    tran0.writeAction("slorii X17 X17 12 271")
    tran0.writeAction("slorii X17 X17 12 941")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
