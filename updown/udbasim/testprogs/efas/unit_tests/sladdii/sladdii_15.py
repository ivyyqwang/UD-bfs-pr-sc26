from EFA_v2 import *
def sladdii_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4564094211870798430, 8, 540]
    tran0.writeAction("movir X16 16214")
    tran0.writeAction("slorii X16 X16 12 3768")
    tran0.writeAction("slorii X16 X16 12 267")
    tran0.writeAction("slorii X16 X16 12 3995")
    tran0.writeAction("slorii X16 X16 12 606")
    tran0.writeAction("sladdii X16 X17 8 540")
    tran0.writeAction("yieldt")
    return efa
