from EFA_v2 import *
def divi_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6519499306406304089, 21646]
    tran0.writeAction("movir X16 23161")
    tran0.writeAction("slorii X16 X16 12 3745")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("slorii X16 X16 12 2393")
    tran0.writeAction("divi X16 X17 21646")
    tran0.writeAction("yieldt")
    return efa
