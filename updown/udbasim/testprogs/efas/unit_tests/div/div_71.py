from EFA_v2 import *
def div_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6255851946028945525, 1758725802114031359]
    tran0.writeAction("movir X16 43310")
    tran0.writeAction("slorii X16 X16 12 3068")
    tran0.writeAction("slorii X16 X16 12 3277")
    tran0.writeAction("slorii X16 X16 12 2082")
    tran0.writeAction("slorii X16 X16 12 3979")
    tran0.writeAction("movir X17 6248")
    tran0.writeAction("slorii X17 X17 12 1020")
    tran0.writeAction("slorii X17 X17 12 3204")
    tran0.writeAction("slorii X17 X17 12 1313")
    tran0.writeAction("slorii X17 X17 12 3839")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
