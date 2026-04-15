from EFA_v2 import *
def sraddii_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8258297634784138894, 15, 565]
    tran0.writeAction("movir X16 29339")
    tran0.writeAction("slorii X16 X16 12 1503")
    tran0.writeAction("slorii X16 X16 12 458")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("slorii X16 X16 12 1678")
    tran0.writeAction("sraddii X16 X17 15 565")
    tran0.writeAction("yieldt")
    return efa
