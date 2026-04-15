from EFA_v2 import *
def srsubii_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8543839857215396449, 0, 105]
    tran0.writeAction("movir X16 30353")
    tran0.writeAction("slorii X16 X16 12 3345")
    tran0.writeAction("slorii X16 X16 12 1339")
    tran0.writeAction("slorii X16 X16 12 605")
    tran0.writeAction("slorii X16 X16 12 2657")
    tran0.writeAction("srsubii X16 X17 0 105")
    tran0.writeAction("yieldt")
    return efa
