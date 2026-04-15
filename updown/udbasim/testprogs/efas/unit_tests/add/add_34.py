from EFA_v2 import *
def add_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1536539241746064610, 1611452466643585470]
    tran0.writeAction("movir X16 60077")
    tran0.writeAction("slorii X16 X16 12 475")
    tran0.writeAction("slorii X16 X16 12 856")
    tran0.writeAction("slorii X16 X16 12 1137")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("movir X17 5725")
    tran0.writeAction("slorii X17 X17 12 119")
    tran0.writeAction("slorii X17 X17 12 2822")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("slorii X17 X17 12 2494")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
