from EFA_v2 import *
def slsubii_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [711685293411833032, 9, 829]
    tran0.writeAction("movir X16 2528")
    tran0.writeAction("slorii X16 X16 12 1696")
    tran0.writeAction("slorii X16 X16 12 241")
    tran0.writeAction("slorii X16 X16 12 2793")
    tran0.writeAction("slorii X16 X16 12 1224")
    tran0.writeAction("slsubii X16 X17 9 829")
    tran0.writeAction("yieldt")
    return efa
