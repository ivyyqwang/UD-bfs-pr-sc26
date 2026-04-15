from EFA_v2 import *
def addi_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1416023387153287143, -23441]
    tran0.writeAction("movir X16 5030")
    tran0.writeAction("slorii X16 X16 12 2972")
    tran0.writeAction("slorii X16 X16 12 1192")
    tran0.writeAction("slorii X16 X16 12 3756")
    tran0.writeAction("slorii X16 X16 12 2023")
    tran0.writeAction("addi X16 X17 -23441")
    tran0.writeAction("yieldt")
    return efa
