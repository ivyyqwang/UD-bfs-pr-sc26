from EFA_v2 import *
def sraddii_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8569168927575227994, 5, 688]
    tran0.writeAction("movir X16 35092")
    tran0.writeAction("slorii X16 X16 12 804")
    tran0.writeAction("slorii X16 X16 12 771")
    tran0.writeAction("slorii X16 X16 12 2308")
    tran0.writeAction("slorii X16 X16 12 422")
    tran0.writeAction("sraddii X16 X17 5 688")
    tran0.writeAction("yieldt")
    return efa
