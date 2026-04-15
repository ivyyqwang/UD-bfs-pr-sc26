from EFA_v2 import *
def divi_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2737037868300479689, -21690]
    tran0.writeAction("movir X16 55812")
    tran0.writeAction("slorii X16 X16 12 360")
    tran0.writeAction("slorii X16 X16 12 3947")
    tran0.writeAction("slorii X16 X16 12 645")
    tran0.writeAction("slorii X16 X16 12 823")
    tran0.writeAction("divi X16 X17 -21690")
    tran0.writeAction("yieldt")
    return efa
