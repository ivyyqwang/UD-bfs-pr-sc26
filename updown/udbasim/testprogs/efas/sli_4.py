from EFA_v2 import *
def sli_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -14271")
    tran0.writeAction("slorii X16 X16 12 3461")
    tran0.writeAction("slorii X16 X16 12 3927")
    tran0.writeAction("slorii X16 X16 12 464")
    tran0.writeAction("slorii X16 X16 12 1624")
    tran0.writeAction("movir X17 7408")
    tran0.writeAction("slorii X17 X17 12 786")
    tran0.writeAction("slorii X17 X17 12 2455")
    tran0.writeAction("slorii X17 X17 12 2951")
    tran0.writeAction("slorii X17 X17 12 1422")
    tran0.writeAction("sli X16 X17 57")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
