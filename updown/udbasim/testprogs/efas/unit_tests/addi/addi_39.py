from EFA_v2 import *
def addi_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3881564164289813987, 11990]
    tran0.writeAction("movir X16 13790")
    tran0.writeAction("slorii X16 X16 12 352")
    tran0.writeAction("slorii X16 X16 12 2753")
    tran0.writeAction("slorii X16 X16 12 1557")
    tran0.writeAction("slorii X16 X16 12 3555")
    tran0.writeAction("addi X16 X17 11990")
    tran0.writeAction("yieldt")
    return efa
