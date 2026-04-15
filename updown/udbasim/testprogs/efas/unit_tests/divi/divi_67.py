from EFA_v2 import *
def divi_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3179239860147789273, 20653]
    tran0.writeAction("movir X16 11294")
    tran0.writeAction("slorii X16 X16 12 3804")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("slorii X16 X16 12 3569")
    tran0.writeAction("slorii X16 X16 12 3545")
    tran0.writeAction("divi X16 X17 20653")
    tran0.writeAction("yieldt")
    return efa
