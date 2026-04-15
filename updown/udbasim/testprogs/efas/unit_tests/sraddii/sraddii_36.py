from EFA_v2 import *
def sraddii_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3328625064236869782, 9, 932]
    tran0.writeAction("movir X16 11825")
    tran0.writeAction("slorii X16 X16 12 2669")
    tran0.writeAction("slorii X16 X16 12 3120")
    tran0.writeAction("slorii X16 X16 12 1230")
    tran0.writeAction("slorii X16 X16 12 2198")
    tran0.writeAction("sraddii X16 X17 9 932")
    tran0.writeAction("yieldt")
    return efa
