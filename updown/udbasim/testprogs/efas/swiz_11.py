from EFA_v2 import *
def swiz_11():
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
    tran0.writeAction("slorii X16 X16 12 1008")
    tran0.writeAction("slorii X16 X16 12 1023")
    tran0.writeAction("movir X17 12277")
    tran0.writeAction("slorii X17 X17 12 4052")
    tran0.writeAction("slorii X17 X17 12 1275")
    tran0.writeAction("slorii X17 X17 12 2778")
    tran0.writeAction("slorii X17 X17 12 310")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("swiz X16 X17")
    tran0.writeAction("yieldt")
    return efa
