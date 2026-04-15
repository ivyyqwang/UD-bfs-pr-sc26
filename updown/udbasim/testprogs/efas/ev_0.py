from EFA_v2 import *
def ev_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 663331
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 4769")
    tran0.writeAction("slorii X16 X16 12 2474")
    tran0.writeAction("slorii X16 X16 12 3735")
    tran0.writeAction("slorii X16 X16 12 3656")
    tran0.writeAction("slorii X16 X16 12 1320")
    tran0.writeAction("movir X17 11037")
    tran0.writeAction("slorii X17 X17 12 540")
    tran0.writeAction("slorii X17 X17 12 52")
    tran0.writeAction("slorii X17 X17 12 3035")
    tran0.writeAction("slorii X17 X17 12 2874")
    tran0.writeAction("movir X18 1781")
    tran0.writeAction("slorii X18 X18 12 2425")
    tran0.writeAction("slorii X18 X18 12 624")
    tran0.writeAction("slorii X18 X18 12 417")
    tran0.writeAction("slorii X18 X18 12 3875")
    tran0.writeAction("movir X19 -32695")
    tran0.writeAction("slorii X19 X19 12 3683")
    tran0.writeAction("slorii X19 X19 12 494")
    tran0.writeAction("slorii X19 X19 12 1493")
    tran0.writeAction("slorii X19 X19 12 3424")
    tran0.writeAction("ev X16 X17 X18 X19 1")
    tran0.writeAction(f"print '%d,%d,%d,%d' X16 X17 X18 X19")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
