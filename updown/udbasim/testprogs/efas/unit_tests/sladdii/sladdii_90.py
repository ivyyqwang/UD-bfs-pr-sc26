from EFA_v2 import *
def sladdii_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9074514888639215237, 5, 1696]
    tran0.writeAction("movir X16 32239")
    tran0.writeAction("slorii X16 X16 12 627")
    tran0.writeAction("slorii X16 X16 12 1630")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("slorii X16 X16 12 1669")
    tran0.writeAction("sladdii X16 X17 5 1696")
    tran0.writeAction("yieldt")
    return efa
