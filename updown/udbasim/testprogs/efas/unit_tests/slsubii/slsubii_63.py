from EFA_v2 import *
def slsubii_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5962125071060805429, 13, 682]
    tran0.writeAction("movir X16 44354")
    tran0.writeAction("slorii X16 X16 12 1133")
    tran0.writeAction("slorii X16 X16 12 1576")
    tran0.writeAction("slorii X16 X16 12 3973")
    tran0.writeAction("slorii X16 X16 12 2251")
    tran0.writeAction("slsubii X16 X17 13 682")
    tran0.writeAction("yieldt")
    return efa
