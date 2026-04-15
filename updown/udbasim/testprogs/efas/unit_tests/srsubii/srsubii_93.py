from EFA_v2 import *
def srsubii_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8935085873667504502, 15, 811]
    tran0.writeAction("movir X16 33792")
    tran0.writeAction("slorii X16 X16 12 811")
    tran0.writeAction("slorii X16 X16 12 3310")
    tran0.writeAction("slorii X16 X16 12 1792")
    tran0.writeAction("slorii X16 X16 12 1674")
    tran0.writeAction("srsubii X16 X17 15 811")
    tran0.writeAction("yieldt")
    return efa
