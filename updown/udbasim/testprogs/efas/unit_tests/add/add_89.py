from EFA_v2 import *
def add_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3312809964342058392, 7293722655344247612]
    tran0.writeAction("movir X16 11769")
    tran0.writeAction("slorii X16 X16 12 1905")
    tran0.writeAction("slorii X16 X16 12 3148")
    tran0.writeAction("slorii X16 X16 12 4025")
    tran0.writeAction("slorii X16 X16 12 3480")
    tran0.writeAction("movir X17 25912")
    tran0.writeAction("slorii X17 X17 12 2081")
    tran0.writeAction("slorii X17 X17 12 3194")
    tran0.writeAction("slorii X17 X17 12 52")
    tran0.writeAction("slorii X17 X17 12 828")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
