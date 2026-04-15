from EFA_v2 import *
def sli_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -14078")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 3893")
    tran0.writeAction("slorii X16 X16 12 1816")
    tran0.writeAction("slorii X16 X16 12 2047")
    tran0.writeAction("movir X17 -9445")
    tran0.writeAction("slorii X17 X17 12 2475")
    tran0.writeAction("slorii X17 X17 12 3867")
    tran0.writeAction("slorii X17 X17 12 275")
    tran0.writeAction("slorii X17 X17 12 1999")
    tran0.writeAction("sli X16 X17 36")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
