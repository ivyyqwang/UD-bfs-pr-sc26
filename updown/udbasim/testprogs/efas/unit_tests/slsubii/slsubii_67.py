from EFA_v2 import *
def slsubii_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8060692770894509383, 5, 1984]
    tran0.writeAction("movir X16 28637")
    tran0.writeAction("slorii X16 X16 12 1365")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 2975")
    tran0.writeAction("slorii X16 X16 12 1351")
    tran0.writeAction("slsubii X16 X17 5 1984")
    tran0.writeAction("yieldt")
    return efa
