from EFA_v2 import *
def sri_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -25089")
    tran0.writeAction("slorii X16 X16 12 429")
    tran0.writeAction("slorii X16 X16 12 2793")
    tran0.writeAction("slorii X16 X16 12 1866")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("movir X17 23945")
    tran0.writeAction("slorii X17 X17 12 3602")
    tran0.writeAction("slorii X17 X17 12 815")
    tran0.writeAction("slorii X17 X17 12 3516")
    tran0.writeAction("slorii X17 X17 12 1218")
    tran0.writeAction("sri X16 X17 19")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
