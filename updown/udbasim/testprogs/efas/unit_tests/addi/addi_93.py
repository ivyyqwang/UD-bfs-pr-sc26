from EFA_v2 import *
def addi_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2755006765231480623, 1409]
    tran0.writeAction("movir X16 9787")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("slorii X16 X16 12 3691")
    tran0.writeAction("slorii X16 X16 12 1721")
    tran0.writeAction("slorii X16 X16 12 3887")
    tran0.writeAction("addi X16 X17 1409")
    tran0.writeAction("yieldt")
    return efa
