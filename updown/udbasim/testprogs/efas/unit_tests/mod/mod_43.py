from EFA_v2 import *
def mod_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4115707771774539889, 2772687323637084886]
    tran0.writeAction("movir X16 14621")
    tran0.writeAction("slorii X16 X16 12 3814")
    tran0.writeAction("slorii X16 X16 12 2455")
    tran0.writeAction("slorii X16 X16 12 3833")
    tran0.writeAction("slorii X16 X16 12 2161")
    tran0.writeAction("movir X17 9850")
    tran0.writeAction("slorii X17 X17 12 2310")
    tran0.writeAction("slorii X17 X17 12 3638")
    tran0.writeAction("slorii X17 X17 12 2527")
    tran0.writeAction("slorii X17 X17 12 726")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
