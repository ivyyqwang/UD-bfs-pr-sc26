from EFA_v2 import *
def sraddii_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3481261618430081020, 10, 598]
    tran0.writeAction("movir X16 53168")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("slorii X16 X16 12 1120")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("sraddii X16 X17 10 598")
    tran0.writeAction("yieldt")
    return efa
