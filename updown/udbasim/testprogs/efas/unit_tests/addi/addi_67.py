from EFA_v2 import *
def addi_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8080783452413260678, -18658]
    tran0.writeAction("movir X16 28708")
    tran0.writeAction("slorii X16 X16 12 2907")
    tran0.writeAction("slorii X16 X16 12 3187")
    tran0.writeAction("slorii X16 X16 12 3879")
    tran0.writeAction("slorii X16 X16 12 902")
    tran0.writeAction("addi X16 X17 -18658")
    tran0.writeAction("yieldt")
    return efa
