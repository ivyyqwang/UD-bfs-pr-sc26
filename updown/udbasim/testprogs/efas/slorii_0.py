from EFA_v2 import *
def slorii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -3120")
    tran0.writeAction("slorii X16 X16 12 506")
    tran0.writeAction("slorii X16 X16 12 255")
    tran0.writeAction("slorii X16 X16 12 22")
    tran0.writeAction("slorii X16 X16 12 3225")
    tran0.writeAction("movir X17 9901")
    tran0.writeAction("slorii X17 X17 12 2564")
    tran0.writeAction("slorii X17 X17 12 4083")
    tran0.writeAction("slorii X17 X17 12 3316")
    tran0.writeAction("slorii X17 X17 12 933")
    tran0.writeAction("slorii X16 X17 0 4078")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
