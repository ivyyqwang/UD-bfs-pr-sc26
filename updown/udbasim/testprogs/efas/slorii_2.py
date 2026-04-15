from EFA_v2 import *
def slorii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 5598")
    tran0.writeAction("slorii X16 X16 12 1658")
    tran0.writeAction("slorii X16 X16 12 3135")
    tran0.writeAction("slorii X16 X16 12 2246")
    tran0.writeAction("slorii X16 X16 12 2156")
    tran0.writeAction("movir X17 -26279")
    tran0.writeAction("slorii X17 X17 12 1039")
    tran0.writeAction("slorii X17 X17 12 3669")
    tran0.writeAction("slorii X17 X17 12 382")
    tran0.writeAction("slorii X17 X17 12 3929")
    tran0.writeAction("slorii X16 X17 2 1969")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
