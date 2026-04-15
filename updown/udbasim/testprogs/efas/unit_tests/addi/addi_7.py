from EFA_v2 import *
def addi_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4860831571257004960, 16687]
    tran0.writeAction("movir X16 48266")
    tran0.writeAction("slorii X16 X16 12 3511")
    tran0.writeAction("slorii X16 X16 12 146")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 3168")
    tran0.writeAction("addi X16 X17 16687")
    tran0.writeAction("yieldt")
    return efa
