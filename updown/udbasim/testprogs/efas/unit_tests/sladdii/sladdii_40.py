from EFA_v2 import *
def sladdii_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5225294399789659423, 10, 634]
    tran0.writeAction("movir X16 18563")
    tran0.writeAction("slorii X16 X16 12 3993")
    tran0.writeAction("slorii X16 X16 12 610")
    tran0.writeAction("slorii X16 X16 12 1231")
    tran0.writeAction("slorii X16 X16 12 1311")
    tran0.writeAction("sladdii X16 X17 10 634")
    tran0.writeAction("yieldt")
    return efa
