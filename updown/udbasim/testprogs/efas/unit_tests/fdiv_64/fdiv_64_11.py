from EFA_v2 import *
def fdiv_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5327401117104724401, 8264553638609421538]
    tran0.writeAction("movir X16 18926")
    tran0.writeAction("slorii X16 X16 12 2993")
    tran0.writeAction("slorii X16 X16 12 1817")
    tran0.writeAction("slorii X16 X16 12 189")
    tran0.writeAction("slorii X16 X16 12 2481")
    tran0.writeAction("movir X17 29361")
    tran0.writeAction("slorii X17 X17 12 2427")
    tran0.writeAction("slorii X17 X17 12 3888")
    tran0.writeAction("slorii X17 X17 12 1952")
    tran0.writeAction("slorii X17 X17 12 1250")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
