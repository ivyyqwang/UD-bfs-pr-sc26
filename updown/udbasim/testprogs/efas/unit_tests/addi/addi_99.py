from EFA_v2 import *
def addi_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3010168374571505213, 32268]
    tran0.writeAction("movir X16 54841")
    tran0.writeAction("slorii X16 X16 12 3004")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("slorii X16 X16 12 2499")
    tran0.writeAction("addi X16 X17 32268")
    tran0.writeAction("yieldt")
    return efa
