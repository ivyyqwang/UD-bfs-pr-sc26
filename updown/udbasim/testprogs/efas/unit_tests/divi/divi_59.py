from EFA_v2 import *
def divi_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3465588098346006593, 11360]
    tran0.writeAction("movir X16 12312")
    tran0.writeAction("slorii X16 X16 12 992")
    tran0.writeAction("slorii X16 X16 12 915")
    tran0.writeAction("slorii X16 X16 12 3011")
    tran0.writeAction("slorii X16 X16 12 2113")
    tran0.writeAction("divi X16 X17 11360")
    tran0.writeAction("yieldt")
    return efa
