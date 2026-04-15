from EFA_v2 import *
def divi_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7661867349967433227, -15188]
    tran0.writeAction("movir X16 38315")
    tran0.writeAction("slorii X16 X16 12 2371")
    tran0.writeAction("slorii X16 X16 12 3409")
    tran0.writeAction("slorii X16 X16 12 113")
    tran0.writeAction("slorii X16 X16 12 501")
    tran0.writeAction("divi X16 X17 -15188")
    tran0.writeAction("yieldt")
    return efa
