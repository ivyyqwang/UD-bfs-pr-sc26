from EFA_v2 import *
def slsubii_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8579559313852378614, 15, 1577]
    tran0.writeAction("movir X16 30480")
    tran0.writeAction("slorii X16 X16 12 2939")
    tran0.writeAction("slorii X16 X16 12 3407")
    tran0.writeAction("slorii X16 X16 12 2314")
    tran0.writeAction("slorii X16 X16 12 3574")
    tran0.writeAction("slsubii X16 X17 15 1577")
    tran0.writeAction("yieldt")
    return efa
