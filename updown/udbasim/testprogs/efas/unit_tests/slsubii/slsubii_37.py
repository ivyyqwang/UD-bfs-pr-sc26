from EFA_v2 import *
def slsubii_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8642590043480448483, 15, 1389]
    tran0.writeAction("movir X16 34831")
    tran0.writeAction("slorii X16 X16 12 1442")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("slorii X16 X16 12 82")
    tran0.writeAction("slorii X16 X16 12 541")
    tran0.writeAction("slsubii X16 X17 15 1389")
    tran0.writeAction("yieldt")
    return efa
