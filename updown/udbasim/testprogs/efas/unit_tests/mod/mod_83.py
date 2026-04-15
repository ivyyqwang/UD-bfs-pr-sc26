from EFA_v2 import *
def mod_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4678658685406495702, 2396395197191109255]
    tran0.writeAction("movir X16 16621")
    tran0.writeAction("slorii X16 X16 12 3828")
    tran0.writeAction("slorii X16 X16 12 2344")
    tran0.writeAction("slorii X16 X16 12 3892")
    tran0.writeAction("slorii X16 X16 12 982")
    tran0.writeAction("movir X17 8513")
    tran0.writeAction("slorii X17 X17 12 2891")
    tran0.writeAction("slorii X17 X17 12 3126")
    tran0.writeAction("slorii X17 X17 12 115")
    tran0.writeAction("slorii X17 X17 12 2695")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
