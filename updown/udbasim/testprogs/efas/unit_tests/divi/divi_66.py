from EFA_v2 import *
def divi_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2693985201099773008, -15088]
    tran0.writeAction("movir X16 9570")
    tran0.writeAction("slorii X16 X16 12 3924")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("slorii X16 X16 12 2913")
    tran0.writeAction("slorii X16 X16 12 1104")
    tran0.writeAction("divi X16 X17 -15088")
    tran0.writeAction("yieldt")
    return efa
