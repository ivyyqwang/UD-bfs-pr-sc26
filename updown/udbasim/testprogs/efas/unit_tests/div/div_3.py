from EFA_v2 import *
def div_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6601758689064668025, -7301815111545121706]
    tran0.writeAction("movir X16 42081")
    tran0.writeAction("slorii X16 X16 12 3447")
    tran0.writeAction("slorii X16 X16 12 813")
    tran0.writeAction("slorii X16 X16 12 1851")
    tran0.writeAction("slorii X16 X16 12 1159")
    tran0.writeAction("movir X17 39594")
    tran0.writeAction("slorii X17 X17 12 3037")
    tran0.writeAction("slorii X17 X17 12 1980")
    tran0.writeAction("slorii X17 X17 12 3169")
    tran0.writeAction("slorii X17 X17 12 1110")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
