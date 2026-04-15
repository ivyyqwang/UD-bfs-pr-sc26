from EFA_v2 import *
def slsubii_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5281781607285555792, 14, 382]
    tran0.writeAction("movir X16 18764")
    tran0.writeAction("slorii X16 X16 12 2694")
    tran0.writeAction("slorii X16 X16 12 835")
    tran0.writeAction("slorii X16 X16 12 1832")
    tran0.writeAction("slorii X16 X16 12 592")
    tran0.writeAction("slsubii X16 X17 14 382")
    tran0.writeAction("yieldt")
    return efa
