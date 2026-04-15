from EFA_v2 import *
def div_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6794027435069260541, -6575116600758331072]
    tran0.writeAction("movir X16 24137")
    tran0.writeAction("slorii X16 X16 12 959")
    tran0.writeAction("slorii X16 X16 12 1205")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("slorii X16 X16 12 765")
    tran0.writeAction("movir X17 42176")
    tran0.writeAction("slorii X17 X17 12 2020")
    tran0.writeAction("slorii X17 X17 12 2495")
    tran0.writeAction("slorii X17 X17 12 105")
    tran0.writeAction("slorii X17 X17 12 2368")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
