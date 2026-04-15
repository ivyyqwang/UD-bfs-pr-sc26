from EFA_v2 import *
def sari_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 30512")
    tran0.writeAction("slorii X16 X16 12 903")
    tran0.writeAction("slorii X16 X16 12 448")
    tran0.writeAction("slorii X16 X16 12 3180")
    tran0.writeAction("slorii X16 X16 12 2903")
    tran0.writeAction("movir X17 8831")
    tran0.writeAction("slorii X17 X17 12 3574")
    tran0.writeAction("slorii X17 X17 12 2371")
    tran0.writeAction("slorii X17 X17 12 2967")
    tran0.writeAction("slorii X17 X17 12 353")
    tran0.writeAction("sari X16 X17 46")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
