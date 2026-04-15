from EFA_v2 import *
def slsubii_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6872740527649520483, 3, 568]
    tran0.writeAction("movir X16 41119")
    tran0.writeAction("slorii X16 X16 12 494")
    tran0.writeAction("slorii X16 X16 12 1864")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("slorii X16 X16 12 1181")
    tran0.writeAction("slsubii X16 X17 3 568")
    tran0.writeAction("yieldt")
    return efa
