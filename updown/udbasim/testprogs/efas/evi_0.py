from EFA_v2 import *
def evi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 408
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 25352")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("slorii X16 X16 12 1807")
    tran0.writeAction("slorii X16 X16 12 3996")
    tran0.writeAction("slorii X16 X16 12 2732")
    tran0.writeAction("movir X17 31254")
    tran0.writeAction("slorii X17 X17 12 2334")
    tran0.writeAction("slorii X17 X17 12 3493")
    tran0.writeAction("slorii X17 X17 12 1363")
    tran0.writeAction("slorii X17 X17 12 1301")
    tran0.writeAction("evi X16 X17 408 2")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
