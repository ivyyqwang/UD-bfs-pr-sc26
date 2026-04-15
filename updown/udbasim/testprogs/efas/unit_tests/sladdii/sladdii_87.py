from EFA_v2 import *
def sladdii_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8442605666325168421, 15, 380]
    tran0.writeAction("movir X16 29994")
    tran0.writeAction("slorii X16 X16 12 657")
    tran0.writeAction("slorii X16 X16 12 3944")
    tran0.writeAction("slorii X16 X16 12 48")
    tran0.writeAction("slorii X16 X16 12 293")
    tran0.writeAction("sladdii X16 X17 15 380")
    tran0.writeAction("yieldt")
    return efa
