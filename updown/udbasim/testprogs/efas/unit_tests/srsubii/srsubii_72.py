from EFA_v2 import *
def srsubii_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3510543835304006910, 14, 1023]
    tran0.writeAction("movir X16 53064")
    tran0.writeAction("slorii X16 X16 12 175")
    tran0.writeAction("slorii X16 X16 12 2880")
    tran0.writeAction("slorii X16 X16 12 1094")
    tran0.writeAction("slorii X16 X16 12 2818")
    tran0.writeAction("srsubii X16 X17 14 1023")
    tran0.writeAction("yieldt")
    return efa
