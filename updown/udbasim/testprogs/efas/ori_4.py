from EFA_v2 import *
def ori_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 30577")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("slorii X16 X16 12 3624")
    tran0.writeAction("slorii X16 X16 12 3104")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("movir X17 -5427")
    tran0.writeAction("slorii X17 X17 12 199")
    tran0.writeAction("slorii X17 X17 12 2711")
    tran0.writeAction("slorii X17 X17 12 3407")
    tran0.writeAction("slorii X17 X17 12 2492")
    tran0.writeAction("ori X16 X17 3740")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
