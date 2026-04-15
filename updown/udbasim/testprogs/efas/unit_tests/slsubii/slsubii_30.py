from EFA_v2 import *
def slsubii_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5135236232708998632, 0, 1853]
    tran0.writeAction("movir X16 47291")
    tran0.writeAction("slorii X16 X16 12 3997")
    tran0.writeAction("slorii X16 X16 12 2719")
    tran0.writeAction("slorii X16 X16 12 2723")
    tran0.writeAction("slorii X16 X16 12 2584")
    tran0.writeAction("slsubii X16 X17 0 1853")
    tran0.writeAction("yieldt")
    return efa
