from EFA_v2 import *
def divi_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6416508854598753823, -17127]
    tran0.writeAction("movir X16 22796")
    tran0.writeAction("slorii X16 X16 12 76")
    tran0.writeAction("slorii X16 X16 12 3744")
    tran0.writeAction("slorii X16 X16 12 2077")
    tran0.writeAction("slorii X16 X16 12 3615")
    tran0.writeAction("divi X16 X17 -17127")
    tran0.writeAction("yieldt")
    return efa
