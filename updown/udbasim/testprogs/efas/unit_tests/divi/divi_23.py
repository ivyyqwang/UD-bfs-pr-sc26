from EFA_v2 import *
def divi_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1463882188613417689, -25626]
    tran0.writeAction("movir X16 5200")
    tran0.writeAction("slorii X16 X16 12 3089")
    tran0.writeAction("slorii X16 X16 12 2101")
    tran0.writeAction("slorii X16 X16 12 1327")
    tran0.writeAction("slorii X16 X16 12 2777")
    tran0.writeAction("divi X16 X17 -25626")
    tran0.writeAction("yieldt")
    return efa
