from EFA_v2 import *
def ori_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -18356")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("slorii X16 X16 12 2083")
    tran0.writeAction("slorii X16 X16 12 2167")
    tran0.writeAction("slorii X16 X16 12 1159")
    tran0.writeAction("movir X17 6373")
    tran0.writeAction("slorii X17 X17 12 3789")
    tran0.writeAction("slorii X17 X17 12 2560")
    tran0.writeAction("slorii X17 X17 12 19")
    tran0.writeAction("slorii X17 X17 12 1640")
    tran0.writeAction("ori X16 X17 -3707")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
