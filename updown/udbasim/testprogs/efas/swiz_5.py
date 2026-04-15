from EFA_v2 import *
def swiz_5():
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
    tran0.writeAction("slorii X16 X16 12 897")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("movir X17 55026")
    tran0.writeAction("slorii X17 X17 12 1684")
    tran0.writeAction("slorii X17 X17 12 634")
    tran0.writeAction("slorii X17 X17 12 3089")
    tran0.writeAction("slorii X17 X17 12 488")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("swiz X16 X17")
    tran0.writeAction("yieldt")
    return efa
