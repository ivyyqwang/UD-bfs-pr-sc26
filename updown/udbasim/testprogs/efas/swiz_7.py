from EFA_v2 import *
def swiz_7():
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
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("slorii X16 X16 12 511")
    tran0.writeAction("movir X17 51785")
    tran0.writeAction("slorii X17 X17 12 3718")
    tran0.writeAction("slorii X17 X17 12 2722")
    tran0.writeAction("slorii X17 X17 12 1623")
    tran0.writeAction("slorii X17 X17 12 1014")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("swiz X16 X17")
    tran0.writeAction("yieldt")
    return efa
