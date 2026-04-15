from EFA_v2 import *
def slsubii_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4937941998279441131, 3, 1548]
    tran0.writeAction("movir X16 47992")
    tran0.writeAction("slorii X16 X16 12 3710")
    tran0.writeAction("slorii X16 X16 12 2615")
    tran0.writeAction("slorii X16 X16 12 292")
    tran0.writeAction("slorii X16 X16 12 1301")
    tran0.writeAction("slsubii X16 X17 3 1548")
    tran0.writeAction("yieldt")
    return efa
