from EFA_v2 import *
def sraddii_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3746097590638110099, 13, 1538]
    tran0.writeAction("movir X16 52227")
    tran0.writeAction("slorii X16 X16 12 769")
    tran0.writeAction("slorii X16 X16 12 1736")
    tran0.writeAction("slorii X16 X16 12 281")
    tran0.writeAction("slorii X16 X16 12 2669")
    tran0.writeAction("sraddii X16 X17 13 1538")
    tran0.writeAction("yieldt")
    return efa
