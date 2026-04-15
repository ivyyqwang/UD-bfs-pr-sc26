from EFA_v2 import *
def addi_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4555416219525882785, 11446]
    tran0.writeAction("movir X16 49351")
    tran0.writeAction("slorii X16 X16 12 3729")
    tran0.writeAction("slorii X16 X16 12 1407")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 3167")
    tran0.writeAction("addi X16 X17 11446")
    tran0.writeAction("yieldt")
    return efa
