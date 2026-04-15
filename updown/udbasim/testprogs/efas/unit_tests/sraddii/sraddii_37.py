from EFA_v2 import *
def sraddii_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8837868029323138611, 0, 553]
    tran0.writeAction("movir X16 31398")
    tran0.writeAction("slorii X16 X16 12 1698")
    tran0.writeAction("slorii X16 X16 12 1483")
    tran0.writeAction("slorii X16 X16 12 2405")
    tran0.writeAction("slorii X16 X16 12 1587")
    tran0.writeAction("sraddii X16 X17 0 553")
    tran0.writeAction("yieldt")
    return efa
