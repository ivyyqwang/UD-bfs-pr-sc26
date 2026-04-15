from EFA_v2 import *
def add_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5217787489742790014, 5517402175506506344]
    tran0.writeAction("movir X16 46998")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("slorii X16 X16 12 3152")
    tran0.writeAction("slorii X16 X16 12 1654")
    tran0.writeAction("slorii X16 X16 12 642")
    tran0.writeAction("movir X17 19601")
    tran0.writeAction("slorii X17 X17 12 3072")
    tran0.writeAction("slorii X17 X17 12 3026")
    tran0.writeAction("slorii X17 X17 12 134")
    tran0.writeAction("slorii X17 X17 12 616")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
