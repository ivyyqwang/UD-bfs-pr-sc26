from EFA_v2 import *
def slsubii_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5142735420075908334, 12, 1245]
    tran0.writeAction("movir X16 47265")
    tran0.writeAction("slorii X16 X16 12 1366")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 2278")
    tran0.writeAction("slorii X16 X16 12 786")
    tran0.writeAction("slsubii X16 X17 12 1245")
    tran0.writeAction("yieldt")
    return efa
