from EFA_v2 import *
def add_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6923831347273275436, -8642887410531808386]
    tran0.writeAction("movir X16 24598")
    tran0.writeAction("slorii X16 X16 12 1598")
    tran0.writeAction("slorii X16 X16 12 3362")
    tran0.writeAction("slorii X16 X16 12 3841")
    tran0.writeAction("slorii X16 X16 12 2092")
    tran0.writeAction("movir X17 34830")
    tran0.writeAction("slorii X17 X17 12 1211")
    tran0.writeAction("slorii X17 X17 12 301")
    tran0.writeAction("slorii X17 X17 12 2276")
    tran0.writeAction("slorii X17 X17 12 2942")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
