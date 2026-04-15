from EFA_v2 import *
def sraddii_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3917169627243443237, 7, 1913]
    tran0.writeAction("movir X16 51619")
    tran0.writeAction("slorii X16 X16 12 1711")
    tran0.writeAction("slorii X16 X16 12 2659")
    tran0.writeAction("slorii X16 X16 12 840")
    tran0.writeAction("slorii X16 X16 12 3035")
    tran0.writeAction("sraddii X16 X17 7 1913")
    tran0.writeAction("yieldt")
    return efa
