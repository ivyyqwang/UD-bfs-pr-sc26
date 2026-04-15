from EFA_v2 import *
def slsubii_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6198062235534854224, 11, 1248]
    tran0.writeAction("movir X16 43516")
    tran0.writeAction("slorii X16 X16 12 243")
    tran0.writeAction("slorii X16 X16 12 3147")
    tran0.writeAction("slorii X16 X16 12 743")
    tran0.writeAction("slorii X16 X16 12 1968")
    tran0.writeAction("slsubii X16 X17 11 1248")
    tran0.writeAction("yieldt")
    return efa
