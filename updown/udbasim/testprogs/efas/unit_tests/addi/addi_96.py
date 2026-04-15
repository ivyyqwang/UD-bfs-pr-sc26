from EFA_v2 import *
def addi_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8927763192863322246, -2355]
    tran0.writeAction("movir X16 33818")
    tran0.writeAction("slorii X16 X16 12 874")
    tran0.writeAction("slorii X16 X16 12 3434")
    tran0.writeAction("slorii X16 X16 12 2352")
    tran0.writeAction("slorii X16 X16 12 3962")
    tran0.writeAction("addi X16 X17 -2355")
    tran0.writeAction("yieldt")
    return efa
