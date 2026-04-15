from EFA_v2 import *
def slsubii_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8451267190445576361, 12, 1467]
    tran0.writeAction("movir X16 30024")
    tran0.writeAction("slorii X16 X16 12 3819")
    tran0.writeAction("slorii X16 X16 12 2980")
    tran0.writeAction("slorii X16 X16 12 1729")
    tran0.writeAction("slorii X16 X16 12 169")
    tran0.writeAction("slsubii X16 X17 12 1467")
    tran0.writeAction("yieldt")
    return efa
