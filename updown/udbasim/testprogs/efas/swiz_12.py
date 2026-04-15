from EFA_v2 import *
def swiz_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 1023")
    tran0.writeAction("slorii X16 X16 12 63")
    tran0.writeAction("movir X17 1090")
    tran0.writeAction("slorii X17 X17 12 1057")
    tran0.writeAction("slorii X17 X17 12 1262")
    tran0.writeAction("slorii X17 X17 12 3996")
    tran0.writeAction("slorii X17 X17 12 3999")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("swiz X16 X17")
    tran0.writeAction("yieldt")
    return efa
