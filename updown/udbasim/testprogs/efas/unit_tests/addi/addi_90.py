from EFA_v2 import *
def addi_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7996583967509376546, 20875]
    tran0.writeAction("movir X16 28409")
    tran0.writeAction("slorii X16 X16 12 2348")
    tran0.writeAction("slorii X16 X16 12 47")
    tran0.writeAction("slorii X16 X16 12 4014")
    tran0.writeAction("slorii X16 X16 12 3618")
    tran0.writeAction("addi X16 X17 20875")
    tran0.writeAction("yieldt")
    return efa
