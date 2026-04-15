from EFA_v2 import *
def sli_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -8238")
    tran0.writeAction("slorii X16 X16 12 3902")
    tran0.writeAction("slorii X16 X16 12 396")
    tran0.writeAction("slorii X16 X16 12 671")
    tran0.writeAction("slorii X16 X16 12 1896")
    tran0.writeAction("movir X17 5597")
    tran0.writeAction("slorii X17 X17 12 807")
    tran0.writeAction("slorii X17 X17 12 2444")
    tran0.writeAction("slorii X17 X17 12 3055")
    tran0.writeAction("slorii X17 X17 12 1356")
    tran0.writeAction("sli X16 X17 62")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
