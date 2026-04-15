from EFA_v2 import *
def swiz_19():
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
    tran0.writeAction("movir X17 41114")
    tran0.writeAction("slorii X17 X17 12 3715")
    tran0.writeAction("slorii X17 X17 12 2806")
    tran0.writeAction("slorii X17 X17 12 3330")
    tran0.writeAction("slorii X17 X17 12 1287")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("swiz X16 X17")
    tran0.writeAction("yieldt")
    return efa
