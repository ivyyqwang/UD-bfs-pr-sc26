from EFA_v2 import *
def sladdii_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6369216915847339303, 11, 1167]
    tran0.writeAction("movir X16 42907")
    tran0.writeAction("slorii X16 X16 12 4079")
    tran0.writeAction("slorii X16 X16 12 1513")
    tran0.writeAction("slorii X16 X16 12 2090")
    tran0.writeAction("slorii X16 X16 12 729")
    tran0.writeAction("sladdii X16 X17 11 1167")
    tran0.writeAction("yieldt")
    return efa
