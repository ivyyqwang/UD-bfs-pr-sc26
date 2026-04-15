from EFA_v2 import *
def sraddii_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [616328799027919835, 3, 1792]
    tran0.writeAction("movir X16 2189")
    tran0.writeAction("slorii X16 X16 12 2620")
    tran0.writeAction("slorii X16 X16 12 1786")
    tran0.writeAction("slorii X16 X16 12 3695")
    tran0.writeAction("slorii X16 X16 12 3035")
    tran0.writeAction("sraddii X16 X17 3 1792")
    tran0.writeAction("yieldt")
    return efa
