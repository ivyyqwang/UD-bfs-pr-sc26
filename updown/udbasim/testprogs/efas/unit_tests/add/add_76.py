from EFA_v2 import *
def add_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8194387797456486383, 6502953547167045611]
    tran0.writeAction("movir X16 29112")
    tran0.writeAction("slorii X16 X16 12 1284")
    tran0.writeAction("slorii X16 X16 12 2363")
    tran0.writeAction("slorii X16 X16 12 775")
    tran0.writeAction("slorii X16 X16 12 4079")
    tran0.writeAction("movir X17 23103")
    tran0.writeAction("slorii X17 X17 12 540")
    tran0.writeAction("slorii X17 X17 12 3081")
    tran0.writeAction("slorii X17 X17 12 3105")
    tran0.writeAction("slorii X17 X17 12 2027")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
