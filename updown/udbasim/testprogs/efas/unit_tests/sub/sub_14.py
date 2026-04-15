from EFA_v2 import *
def sub_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5677467045489152475, -2836975815344676874]
    tran0.writeAction("movir X16 20170")
    tran0.writeAction("slorii X16 X16 12 1699")
    tran0.writeAction("slorii X16 X16 12 646")
    tran0.writeAction("slorii X16 X16 12 1505")
    tran0.writeAction("slorii X16 X16 12 475")
    tran0.writeAction("movir X17 55457")
    tran0.writeAction("slorii X17 X17 12 152")
    tran0.writeAction("slorii X17 X17 12 1762")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("slorii X17 X17 12 4086")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
