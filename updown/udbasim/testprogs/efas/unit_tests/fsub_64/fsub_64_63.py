from EFA_v2 import *
def fsub_64_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17490489027714515861, 8283803947100075921]
    tran0.writeAction("movir X16 62138")
    tran0.writeAction("slorii X16 X16 12 2865")
    tran0.writeAction("slorii X16 X16 12 2596")
    tran0.writeAction("slorii X16 X16 12 3240")
    tran0.writeAction("slorii X16 X16 12 917")
    tran0.writeAction("movir X17 29429")
    tran0.writeAction("slorii X17 X17 12 4028")
    tran0.writeAction("slorii X17 X17 12 3303")
    tran0.writeAction("slorii X17 X17 12 3599")
    tran0.writeAction("slorii X17 X17 12 1937")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
