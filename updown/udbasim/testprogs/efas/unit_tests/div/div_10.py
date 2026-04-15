from EFA_v2 import *
def div_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6422266562142986036, -2408104713178693786]
    tran0.writeAction("movir X16 42719")
    tran0.writeAction("slorii X16 X16 12 2153")
    tran0.writeAction("slorii X16 X16 12 1694")
    tran0.writeAction("slorii X16 X16 12 2450")
    tran0.writeAction("slorii X16 X16 12 204")
    tran0.writeAction("movir X17 56980")
    tran0.writeAction("slorii X17 X17 12 2840")
    tran0.writeAction("slorii X17 X17 12 1445")
    tran0.writeAction("slorii X17 X17 12 163")
    tran0.writeAction("slorii X17 X17 12 3942")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
