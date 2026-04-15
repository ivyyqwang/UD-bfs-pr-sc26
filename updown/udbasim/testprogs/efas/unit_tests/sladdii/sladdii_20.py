from EFA_v2 import *
def sladdii_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1846271513271957638, 10, 287]
    tran0.writeAction("movir X16 6559")
    tran0.writeAction("slorii X16 X16 12 1122")
    tran0.writeAction("slorii X16 X16 12 2251")
    tran0.writeAction("slorii X16 X16 12 2039")
    tran0.writeAction("slorii X16 X16 12 2182")
    tran0.writeAction("sladdii X16 X17 10 287")
    tran0.writeAction("yieldt")
    return efa
