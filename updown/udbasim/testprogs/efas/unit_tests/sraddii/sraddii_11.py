from EFA_v2 import *
def sraddii_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1658508937791555978, 6, 686]
    tran0.writeAction("movir X16 5892")
    tran0.writeAction("slorii X16 X16 12 849")
    tran0.writeAction("slorii X16 X16 12 1917")
    tran0.writeAction("slorii X16 X16 12 3588")
    tran0.writeAction("slorii X16 X16 12 2442")
    tran0.writeAction("sraddii X16 X17 6 686")
    tran0.writeAction("yieldt")
    return efa
