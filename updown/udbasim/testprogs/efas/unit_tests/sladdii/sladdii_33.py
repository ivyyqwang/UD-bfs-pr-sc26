from EFA_v2 import *
def sladdii_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1322878966948200182, 8, 296]
    tran0.writeAction("movir X16 4699")
    tran0.writeAction("slorii X16 X16 12 3318")
    tran0.writeAction("slorii X16 X16 12 2393")
    tran0.writeAction("slorii X16 X16 12 3207")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("sladdii X16 X17 8 296")
    tran0.writeAction("yieldt")
    return efa
