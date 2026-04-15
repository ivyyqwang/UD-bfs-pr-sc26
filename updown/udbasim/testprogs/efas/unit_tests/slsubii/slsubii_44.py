from EFA_v2 import *
def slsubii_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8178217483252971309, 7, 1820]
    tran0.writeAction("movir X16 29054")
    tran0.writeAction("slorii X16 X16 12 3543")
    tran0.writeAction("slorii X16 X16 12 2193")
    tran0.writeAction("slorii X16 X16 12 747")
    tran0.writeAction("slorii X16 X16 12 1837")
    tran0.writeAction("slsubii X16 X17 7 1820")
    tran0.writeAction("yieldt")
    return efa
