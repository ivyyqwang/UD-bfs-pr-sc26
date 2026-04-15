from EFA_v2 import *
def addi_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2114965993753409769, 16839]
    tran0.writeAction("movir X16 7513")
    tran0.writeAction("slorii X16 X16 12 3557")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("slorii X16 X16 12 2879")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("addi X16 X17 16839")
    tran0.writeAction("yieldt")
    return efa
