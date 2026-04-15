from EFA_v2 import *
def slsubii_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-319130455695561314, 8, 425]
    tran0.writeAction("movir X16 64402")
    tran0.writeAction("slorii X16 X16 12 904")
    tran0.writeAction("slorii X16 X16 12 2711")
    tran0.writeAction("slorii X16 X16 12 1054")
    tran0.writeAction("slorii X16 X16 12 3486")
    tran0.writeAction("slsubii X16 X17 8 425")
    tran0.writeAction("yieldt")
    return efa
