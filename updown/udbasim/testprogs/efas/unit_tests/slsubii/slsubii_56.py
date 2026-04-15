from EFA_v2 import *
def slsubii_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5726019817696479228, 10, 479]
    tran0.writeAction("movir X16 45193")
    tran0.writeAction("slorii X16 X16 12 373")
    tran0.writeAction("slorii X16 X16 12 69")
    tran0.writeAction("slorii X16 X16 12 1451")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slsubii X16 X17 10 479")
    tran0.writeAction("yieldt")
    return efa
