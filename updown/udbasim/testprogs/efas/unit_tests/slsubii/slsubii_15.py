from EFA_v2 import *
def slsubii_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7046595713288646431, 8, 1712]
    tran0.writeAction("movir X16 25034")
    tran0.writeAction("slorii X16 X16 12 2199")
    tran0.writeAction("slorii X16 X16 12 1918")
    tran0.writeAction("slorii X16 X16 12 1474")
    tran0.writeAction("slorii X16 X16 12 3871")
    tran0.writeAction("slsubii X16 X17 8 1712")
    tran0.writeAction("yieldt")
    return efa
