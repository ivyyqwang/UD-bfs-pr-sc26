from EFA_v2 import *
def sraddii_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-536369373091669732, 12, 550]
    tran0.writeAction("movir X16 63630")
    tran0.writeAction("slorii X16 X16 12 1774")
    tran0.writeAction("slorii X16 X16 12 1440")
    tran0.writeAction("slorii X16 X16 12 1933")
    tran0.writeAction("slorii X16 X16 12 2332")
    tran0.writeAction("sraddii X16 X17 12 550")
    tran0.writeAction("yieldt")
    return efa
