from EFA_v2 import *
def slsubii_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7708959968589286700, 3, 623]
    tran0.writeAction("movir X16 38148")
    tran0.writeAction("slorii X16 X16 12 1116")
    tran0.writeAction("slorii X16 X16 12 156")
    tran0.writeAction("slorii X16 X16 12 2167")
    tran0.writeAction("slorii X16 X16 12 724")
    tran0.writeAction("slsubii X16 X17 3 623")
    tran0.writeAction("yieldt")
    return efa
