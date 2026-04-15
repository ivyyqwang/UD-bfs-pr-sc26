from EFA_v2 import *
def mod_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4515842205986370203, -4014333204061023207]
    tran0.writeAction("movir X16 16043")
    tran0.writeAction("slorii X16 X16 12 2024")
    tran0.writeAction("slorii X16 X16 12 3957")
    tran0.writeAction("slorii X16 X16 12 2187")
    tran0.writeAction("slorii X16 X16 12 667")
    tran0.writeAction("movir X17 51274")
    tran0.writeAction("slorii X17 X17 12 915")
    tran0.writeAction("slorii X17 X17 12 2113")
    tran0.writeAction("slorii X17 X17 12 3633")
    tran0.writeAction("slorii X17 X17 12 1049")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
