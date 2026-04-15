from EFA_v2 import *
def ev_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 29685
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -3698")
    tran0.writeAction("slorii X16 X16 12 164")
    tran0.writeAction("slorii X16 X16 12 1227")
    tran0.writeAction("slorii X16 X16 12 3585")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("movir X17 -23801")
    tran0.writeAction("slorii X17 X17 12 1429")
    tran0.writeAction("slorii X17 X17 12 1951")
    tran0.writeAction("slorii X17 X17 12 2183")
    tran0.writeAction("slorii X17 X17 12 2059")
    tran0.writeAction("movir X18 -3361")
    tran0.writeAction("slorii X18 X18 12 2723")
    tran0.writeAction("slorii X18 X18 12 75")
    tran0.writeAction("slorii X18 X18 12 263")
    tran0.writeAction("slorii X18 X18 12 1013")
    tran0.writeAction("movir X19 -20465")
    tran0.writeAction("slorii X19 X19 12 1456")
    tran0.writeAction("slorii X19 X19 12 2574")
    tran0.writeAction("slorii X19 X19 12 3286")
    tran0.writeAction("slorii X19 X19 12 1069")
    tran0.writeAction("ev X16 X17 X18 X19 4")
    tran0.writeAction(f"print '%d,%d,%d,%d' X16 X17 X18 X19")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
