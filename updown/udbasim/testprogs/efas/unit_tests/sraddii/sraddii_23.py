from EFA_v2 import *
def sraddii_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6273314366664225853, 10, 768]
    tran0.writeAction("movir X16 22287")
    tran0.writeAction("slorii X16 X16 12 1186")
    tran0.writeAction("slorii X16 X16 12 3541")
    tran0.writeAction("slorii X16 X16 12 1539")
    tran0.writeAction("slorii X16 X16 12 1085")
    tran0.writeAction("sraddii X16 X17 10 768")
    tran0.writeAction("yieldt")
    return efa
