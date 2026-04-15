from EFA_v2 import *
def srsubii_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5494623683470256149, 0, 339]
    tran0.writeAction("movir X16 19520")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 219")
    tran0.writeAction("slorii X16 X16 12 2838")
    tran0.writeAction("slorii X16 X16 12 2069")
    tran0.writeAction("srsubii X16 X17 0 339")
    tran0.writeAction("yieldt")
    return efa
