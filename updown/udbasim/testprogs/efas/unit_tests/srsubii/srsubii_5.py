from EFA_v2 import *
def srsubii_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3870003732494498721, 11, 211]
    tran0.writeAction("movir X16 51786")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("slorii X16 X16 12 3077")
    tran0.writeAction("slorii X16 X16 12 940")
    tran0.writeAction("slorii X16 X16 12 1119")
    tran0.writeAction("srsubii X16 X17 11 211")
    tran0.writeAction("yieldt")
    return efa
