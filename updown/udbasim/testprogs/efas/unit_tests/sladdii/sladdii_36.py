from EFA_v2 import *
def sladdii_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4768712458906150559, 9, 1341]
    tran0.writeAction("movir X16 16941")
    tran0.writeAction("slorii X16 X16 12 3563")
    tran0.writeAction("slorii X16 X16 12 1845")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("slorii X16 X16 12 1695")
    tran0.writeAction("sladdii X16 X17 9 1341")
    tran0.writeAction("yieldt")
    return efa
