from EFA_v2 import *
def sladdii_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8839758181868276129, 2, 1765]
    tran0.writeAction("movir X16 31405")
    tran0.writeAction("slorii X16 X16 12 531")
    tran0.writeAction("slorii X16 X16 12 2874")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("sladdii X16 X17 2 1765")
    tran0.writeAction("yieldt")
    return efa
