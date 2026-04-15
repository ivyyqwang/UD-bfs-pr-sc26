from EFA_v2 import *
def addi_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [370462358609655642, -12259]
    tran0.writeAction("movir X16 1316")
    tran0.writeAction("slorii X16 X16 12 600")
    tran0.writeAction("slorii X16 X16 12 3431")
    tran0.writeAction("slorii X16 X16 12 2383")
    tran0.writeAction("slorii X16 X16 12 1882")
    tran0.writeAction("addi X16 X17 -12259")
    tran0.writeAction("yieldt")
    return efa
