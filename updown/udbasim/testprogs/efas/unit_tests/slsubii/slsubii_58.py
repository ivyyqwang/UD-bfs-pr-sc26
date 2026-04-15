from EFA_v2 import *
def slsubii_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6346181134824859213, 7, 1162]
    tran0.writeAction("movir X16 22546")
    tran0.writeAction("slorii X16 X16 12 673")
    tran0.writeAction("slorii X16 X16 12 3677")
    tran0.writeAction("slorii X16 X16 12 2134")
    tran0.writeAction("slorii X16 X16 12 1613")
    tran0.writeAction("slsubii X16 X17 7 1162")
    tran0.writeAction("yieldt")
    return efa
