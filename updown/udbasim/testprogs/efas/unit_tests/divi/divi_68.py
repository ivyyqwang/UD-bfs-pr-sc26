from EFA_v2 import *
def divi_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5772815598244971238, 17462]
    tran0.writeAction("movir X16 45026")
    tran0.writeAction("slorii X16 X16 12 3436")
    tran0.writeAction("slorii X16 X16 12 3216")
    tran0.writeAction("slorii X16 X16 12 3171")
    tran0.writeAction("slorii X16 X16 12 3354")
    tran0.writeAction("divi X16 X17 17462")
    tran0.writeAction("yieldt")
    return efa
