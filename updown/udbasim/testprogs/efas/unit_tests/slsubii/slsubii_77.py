from EFA_v2 import *
def slsubii_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [755944977115874311, 5, 1354]
    tran0.writeAction("movir X16 2685")
    tran0.writeAction("slorii X16 X16 12 2687")
    tran0.writeAction("slorii X16 X16 12 918")
    tran0.writeAction("slorii X16 X16 12 3000")
    tran0.writeAction("slorii X16 X16 12 1031")
    tran0.writeAction("slsubii X16 X17 5 1354")
    tran0.writeAction("yieldt")
    return efa
