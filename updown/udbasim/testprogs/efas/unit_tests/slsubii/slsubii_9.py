from EFA_v2 import *
def slsubii_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7012270552416922865, 12, 1139]
    tran0.writeAction("movir X16 24912")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("slorii X16 X16 12 2609")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("slorii X16 X16 12 3313")
    tran0.writeAction("slsubii X16 X17 12 1139")
    tran0.writeAction("yieldt")
    return efa
