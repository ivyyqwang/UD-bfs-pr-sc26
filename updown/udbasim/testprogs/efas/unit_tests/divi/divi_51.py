from EFA_v2 import *
def divi_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3904813823541950829, -26212]
    tran0.writeAction("movir X16 13872")
    tran0.writeAction("slorii X16 X16 12 2807")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("slorii X16 X16 12 1035")
    tran0.writeAction("slorii X16 X16 12 2413")
    tran0.writeAction("divi X16 X17 -26212")
    tran0.writeAction("yieldt")
    return efa
