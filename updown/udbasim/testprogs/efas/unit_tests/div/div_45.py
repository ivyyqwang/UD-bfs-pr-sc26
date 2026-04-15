from EFA_v2 import *
def div_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1597395099713543952, 49365263078678388]
    tran0.writeAction("movir X16 5675")
    tran0.writeAction("slorii X16 X16 12 358")
    tran0.writeAction("slorii X16 X16 12 316")
    tran0.writeAction("slorii X16 X16 12 1537")
    tran0.writeAction("slorii X16 X16 12 3856")
    tran0.writeAction("movir X17 175")
    tran0.writeAction("slorii X17 X17 12 1559")
    tran0.writeAction("slorii X17 X17 12 506")
    tran0.writeAction("slorii X17 X17 12 197")
    tran0.writeAction("slorii X17 X17 12 3956")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
