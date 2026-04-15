from EFA_v2 import *
def slori_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 3916")
    tran0.writeAction("slorii X16 X16 12 575")
    tran0.writeAction("slorii X16 X16 12 3569")
    tran0.writeAction("slorii X16 X16 12 957")
    tran0.writeAction("slorii X16 X16 12 3103")
    tran0.writeAction("movir X17 13315")
    tran0.writeAction("slorii X17 X17 12 2224")
    tran0.writeAction("slorii X17 X17 12 3755")
    tran0.writeAction("slorii X17 X17 12 1259")
    tran0.writeAction("slorii X17 X17 12 200")
    tran0.writeAction("slori X16 X17 3")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
