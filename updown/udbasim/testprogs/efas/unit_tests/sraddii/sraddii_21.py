from EFA_v2 import *
def sraddii_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6869741386917326774, 8, 1517]
    tran0.writeAction("movir X16 41129")
    tran0.writeAction("slorii X16 X16 12 3177")
    tran0.writeAction("slorii X16 X16 12 2853")
    tran0.writeAction("slorii X16 X16 12 4069")
    tran0.writeAction("slorii X16 X16 12 74")
    tran0.writeAction("sraddii X16 X17 8 1517")
    tran0.writeAction("yieldt")
    return efa
