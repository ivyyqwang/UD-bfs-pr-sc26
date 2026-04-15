from EFA_v2 import *
def divi_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [540364868653544078, 17242]
    tran0.writeAction("movir X16 1919")
    tran0.writeAction("slorii X16 X16 12 3119")
    tran0.writeAction("slorii X16 X16 12 3117")
    tran0.writeAction("slorii X16 X16 12 799")
    tran0.writeAction("slorii X16 X16 12 654")
    tran0.writeAction("divi X16 X17 17242")
    tran0.writeAction("yieldt")
    return efa
