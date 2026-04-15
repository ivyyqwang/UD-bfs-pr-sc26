from EFA_v2 import *
def divi_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6308548970641441760, -14209]
    tran0.writeAction("movir X16 22412")
    tran0.writeAction("slorii X16 X16 12 1917")
    tran0.writeAction("slorii X16 X16 12 3419")
    tran0.writeAction("slorii X16 X16 12 980")
    tran0.writeAction("slorii X16 X16 12 992")
    tran0.writeAction("divi X16 X17 -14209")
    tran0.writeAction("yieldt")
    return efa
