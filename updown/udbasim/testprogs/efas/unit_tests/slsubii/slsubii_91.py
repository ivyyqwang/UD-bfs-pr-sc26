from EFA_v2 import *
def slsubii_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7034412275064247020, 12, 1413]
    tran0.writeAction("movir X16 24991")
    tran0.writeAction("slorii X16 X16 12 1035")
    tran0.writeAction("slorii X16 X16 12 442")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("slorii X16 X16 12 748")
    tran0.writeAction("slsubii X16 X17 12 1413")
    tran0.writeAction("yieldt")
    return efa
