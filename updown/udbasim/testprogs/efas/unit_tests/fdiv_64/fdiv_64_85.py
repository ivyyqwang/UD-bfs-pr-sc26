from EFA_v2 import *
def fdiv_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9278387820442333897, 5353852333373425756]
    tran0.writeAction("movir X16 32963")
    tran0.writeAction("slorii X16 X16 12 1865")
    tran0.writeAction("slorii X16 X16 12 77")
    tran0.writeAction("slorii X16 X16 12 3179")
    tran0.writeAction("slorii X16 X16 12 713")
    tran0.writeAction("movir X17 19020")
    tran0.writeAction("slorii X17 X17 12 2885")
    tran0.writeAction("slorii X17 X17 12 1230")
    tran0.writeAction("slorii X17 X17 12 2536")
    tran0.writeAction("slorii X17 X17 12 2140")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
