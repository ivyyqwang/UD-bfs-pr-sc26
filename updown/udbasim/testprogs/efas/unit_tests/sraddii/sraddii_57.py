from EFA_v2 import *
def sraddii_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3408115870756294302, 10, 1921]
    tran0.writeAction("movir X16 12108")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("slorii X16 X16 12 981")
    tran0.writeAction("slorii X16 X16 12 3276")
    tran0.writeAction("slorii X16 X16 12 3742")
    tran0.writeAction("sraddii X16 X17 10 1921")
    tran0.writeAction("yieldt")
    return efa
