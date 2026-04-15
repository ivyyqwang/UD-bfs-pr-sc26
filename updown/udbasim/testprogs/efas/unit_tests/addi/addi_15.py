from EFA_v2 import *
def addi_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3237032741219371951, -32754]
    tran0.writeAction("movir X16 11500")
    tran0.writeAction("slorii X16 X16 12 1026")
    tran0.writeAction("slorii X16 X16 12 170")
    tran0.writeAction("slorii X16 X16 12 2824")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("addi X16 X17 -32754")
    tran0.writeAction("yieldt")
    return efa
