from EFA_v2 import *
def addi_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1020550464911312439, 5927]
    tran0.writeAction("movir X16 3625")
    tran0.writeAction("slorii X16 X16 12 2963")
    tran0.writeAction("slorii X16 X16 12 3488")
    tran0.writeAction("slorii X16 X16 12 1632")
    tran0.writeAction("slorii X16 X16 12 1591")
    tran0.writeAction("addi X16 X17 5927")
    tran0.writeAction("yieldt")
    return efa
