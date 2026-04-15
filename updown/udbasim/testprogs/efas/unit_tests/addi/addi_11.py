from EFA_v2 import *
def addi_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6151762479019540650, 27292]
    tran0.writeAction("movir X16 43680")
    tran0.writeAction("slorii X16 X16 12 2249")
    tran0.writeAction("slorii X16 X16 12 3687")
    tran0.writeAction("slorii X16 X16 12 1899")
    tran0.writeAction("slorii X16 X16 12 3926")
    tran0.writeAction("addi X16 X17 27292")
    tran0.writeAction("yieldt")
    return efa
