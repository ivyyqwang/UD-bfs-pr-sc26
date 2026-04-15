from EFA_v2 import *
def slsubii_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5796828290203846946, 15, 1181]
    tran0.writeAction("movir X16 20594")
    tran0.writeAction("slorii X16 X16 12 1929")
    tran0.writeAction("slorii X16 X16 12 3573")
    tran0.writeAction("slorii X16 X16 12 2192")
    tran0.writeAction("slorii X16 X16 12 2338")
    tran0.writeAction("slsubii X16 X17 15 1181")
    tran0.writeAction("yieldt")
    return efa
