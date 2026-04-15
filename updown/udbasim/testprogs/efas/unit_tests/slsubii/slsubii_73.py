from EFA_v2 import *
def slsubii_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [444154766343227079, 15, 927]
    tran0.writeAction("movir X16 1577")
    tran0.writeAction("slorii X16 X16 12 3910")
    tran0.writeAction("slorii X16 X16 12 2081")
    tran0.writeAction("slorii X16 X16 12 756")
    tran0.writeAction("slorii X16 X16 12 1735")
    tran0.writeAction("slsubii X16 X17 15 927")
    tran0.writeAction("yieldt")
    return efa
