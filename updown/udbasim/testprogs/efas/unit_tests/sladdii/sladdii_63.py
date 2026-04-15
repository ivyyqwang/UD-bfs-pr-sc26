from EFA_v2 import *
def sladdii_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-788022416813561400, 13, 1268]
    tran0.writeAction("movir X16 62736")
    tran0.writeAction("slorii X16 X16 12 1564")
    tran0.writeAction("slorii X16 X16 12 2426")
    tran0.writeAction("slorii X16 X16 12 3206")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("sladdii X16 X17 13 1268")
    tran0.writeAction("yieldt")
    return efa
