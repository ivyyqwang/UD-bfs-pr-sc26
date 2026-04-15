from EFA_v2 import *
def slsubii_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5275045165382443054, 3, 908]
    tran0.writeAction("movir X16 46795")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("slorii X16 X16 12 3799")
    tran0.writeAction("slorii X16 X16 12 973")
    tran0.writeAction("slorii X16 X16 12 4050")
    tran0.writeAction("slsubii X16 X17 3 908")
    tran0.writeAction("yieldt")
    return efa
