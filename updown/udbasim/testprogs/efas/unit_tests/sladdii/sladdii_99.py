from EFA_v2 import *
def sladdii_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8671712109341050747, 14, 375]
    tran0.writeAction("movir X16 34727")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 2048")
    tran0.writeAction("slorii X16 X16 12 1119")
    tran0.writeAction("slorii X16 X16 12 2181")
    tran0.writeAction("sladdii X16 X17 14 375")
    tran0.writeAction("yieldt")
    return efa
