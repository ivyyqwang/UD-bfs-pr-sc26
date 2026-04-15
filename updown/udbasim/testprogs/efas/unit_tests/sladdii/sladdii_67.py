from EFA_v2 import *
def sladdii_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7572398069183314844, 15, 59]
    tran0.writeAction("movir X16 26902")
    tran0.writeAction("slorii X16 X16 12 2302")
    tran0.writeAction("slorii X16 X16 12 3187")
    tran0.writeAction("slorii X16 X16 12 2151")
    tran0.writeAction("slorii X16 X16 12 2972")
    tran0.writeAction("sladdii X16 X17 15 59")
    tran0.writeAction("yieldt")
    return efa
