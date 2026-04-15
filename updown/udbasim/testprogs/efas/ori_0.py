from EFA_v2 import *
def ori_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -31023")
    tran0.writeAction("slorii X16 X16 12 4073")
    tran0.writeAction("slorii X16 X16 12 181")
    tran0.writeAction("slorii X16 X16 12 1044")
    tran0.writeAction("slorii X16 X16 12 3754")
    tran0.writeAction("movir X17 -19032")
    tran0.writeAction("slorii X17 X17 12 806")
    tran0.writeAction("slorii X17 X17 12 2180")
    tran0.writeAction("slorii X17 X17 12 2737")
    tran0.writeAction("slorii X17 X17 12 3315")
    tran0.writeAction("ori X16 X17 7721")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
