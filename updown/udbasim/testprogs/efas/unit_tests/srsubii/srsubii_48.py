from EFA_v2 import *
def srsubii_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6064628456296748905, 1, 325]
    tran0.writeAction("movir X16 43990")
    tran0.writeAction("slorii X16 X16 12 456")
    tran0.writeAction("slorii X16 X16 12 3327")
    tran0.writeAction("slorii X16 X16 12 2894")
    tran0.writeAction("slorii X16 X16 12 2199")
    tran0.writeAction("srsubii X16 X17 1 325")
    tran0.writeAction("yieldt")
    return efa
