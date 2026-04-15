from EFA_v2 import *
def sub_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1173722591133471740, -5491111133059054788]
    tran0.writeAction("movir X16 4169")
    tran0.writeAction("slorii X16 X16 12 3687")
    tran0.writeAction("slorii X16 X16 12 2653")
    tran0.writeAction("slorii X16 X16 12 1481")
    tran0.writeAction("slorii X16 X16 12 1020")
    tran0.writeAction("movir X17 46027")
    tran0.writeAction("slorii X17 X17 12 2680")
    tran0.writeAction("slorii X17 X17 12 1155")
    tran0.writeAction("slorii X17 X17 12 3368")
    tran0.writeAction("slorii X17 X17 12 828")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
