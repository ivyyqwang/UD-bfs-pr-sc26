from EFA_v2 import *
def sladdii_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6231738273782614230, 5, 937]
    tran0.writeAction("movir X16 43396")
    tran0.writeAction("slorii X16 X16 12 1712")
    tran0.writeAction("slorii X16 X16 12 3745")
    tran0.writeAction("slorii X16 X16 12 4019")
    tran0.writeAction("slorii X16 X16 12 1834")
    tran0.writeAction("sladdii X16 X17 5 937")
    tran0.writeAction("yieldt")
    return efa
