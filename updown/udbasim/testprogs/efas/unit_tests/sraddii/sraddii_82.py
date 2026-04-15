from EFA_v2 import *
def sraddii_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2074663664241283473, 9, 1515]
    tran0.writeAction("movir X16 7370")
    tran0.writeAction("slorii X16 X16 12 2809")
    tran0.writeAction("slorii X16 X16 12 3151")
    tran0.writeAction("slorii X16 X16 12 2097")
    tran0.writeAction("slorii X16 X16 12 401")
    tran0.writeAction("sraddii X16 X17 9 1515")
    tran0.writeAction("yieldt")
    return efa
