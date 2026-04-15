from EFA_v2 import *
def add_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1436429342576977571, 1544220159897075378]
    tran0.writeAction("movir X16 5103")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 101")
    tran0.writeAction("slorii X16 X16 12 1018")
    tran0.writeAction("slorii X16 X16 12 1699")
    tran0.writeAction("movir X17 5486")
    tran0.writeAction("slorii X17 X17 12 704")
    tran0.writeAction("slorii X17 X17 12 3525")
    tran0.writeAction("slorii X17 X17 12 2711")
    tran0.writeAction("slorii X17 X17 12 3762")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
