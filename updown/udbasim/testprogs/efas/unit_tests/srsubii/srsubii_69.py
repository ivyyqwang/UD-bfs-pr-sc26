from EFA_v2 import *
def srsubii_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-896985884875782053, 6, 1544]
    tran0.writeAction("movir X16 62349")
    tran0.writeAction("slorii X16 X16 12 1089")
    tran0.writeAction("slorii X16 X16 12 1811")
    tran0.writeAction("slorii X16 X16 12 1800")
    tran0.writeAction("slorii X16 X16 12 2139")
    tran0.writeAction("srsubii X16 X17 6 1544")
    tran0.writeAction("yieldt")
    return efa
