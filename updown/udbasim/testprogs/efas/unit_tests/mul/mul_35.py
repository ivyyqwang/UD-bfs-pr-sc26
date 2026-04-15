from EFA_v2 import *
def mul_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6544855902115964539, -7027960770899146147]
    tran0.writeAction("movir X16 23251")
    tran0.writeAction("slorii X16 X16 12 4092")
    tran0.writeAction("slorii X16 X16 12 1103")
    tran0.writeAction("slorii X16 X16 12 3034")
    tran0.writeAction("slorii X16 X16 12 1659")
    tran0.writeAction("movir X17 40567")
    tran0.writeAction("slorii X17 X17 12 2734")
    tran0.writeAction("slorii X17 X17 12 2595")
    tran0.writeAction("slorii X17 X17 12 720")
    tran0.writeAction("slorii X17 X17 12 2653")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
