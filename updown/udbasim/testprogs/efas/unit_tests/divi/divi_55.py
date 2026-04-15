from EFA_v2 import *
def divi_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5270382565344014885, 21667]
    tran0.writeAction("movir X16 18724")
    tran0.writeAction("slorii X16 X16 12 656")
    tran0.writeAction("slorii X16 X16 12 1277")
    tran0.writeAction("slorii X16 X16 12 3039")
    tran0.writeAction("slorii X16 X16 12 549")
    tran0.writeAction("divi X16 X17 21667")
    tran0.writeAction("yieldt")
    return efa
