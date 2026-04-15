from EFA_v2 import *
def fcnvt_64_b16_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4427674872118265101]
    tran0.writeAction("movir X16 15730")
    tran0.writeAction("slorii X16 X16 12 1069")
    tran0.writeAction("slorii X16 X16 12 1629")
    tran0.writeAction("slorii X16 X16 12 2180")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
