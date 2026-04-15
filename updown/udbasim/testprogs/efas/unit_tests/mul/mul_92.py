from EFA_v2 import *
def mul_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4889998104057715356, 6057917624012264596]
    tran0.writeAction("movir X16 17372")
    tran0.writeAction("slorii X16 X16 12 3125")
    tran0.writeAction("slorii X16 X16 12 3592")
    tran0.writeAction("slorii X16 X16 12 2841")
    tran0.writeAction("slorii X16 X16 12 2716")
    tran0.writeAction("movir X17 21522")
    tran0.writeAction("slorii X17 X17 12 191")
    tran0.writeAction("slorii X17 X17 12 2969")
    tran0.writeAction("slorii X17 X17 12 3397")
    tran0.writeAction("slorii X17 X17 12 1172")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
