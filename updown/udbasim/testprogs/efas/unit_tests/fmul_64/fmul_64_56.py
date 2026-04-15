from EFA_v2 import *
def fmul_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3915608501065216214, 185837485379194900]
    tran0.writeAction("movir X16 13911")
    tran0.writeAction("slorii X16 X16 12 146")
    tran0.writeAction("slorii X16 X16 12 3993")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("movir X17 660")
    tran0.writeAction("slorii X17 X17 12 931")
    tran0.writeAction("slorii X17 X17 12 1365")
    tran0.writeAction("slorii X17 X17 12 4009")
    tran0.writeAction("slorii X17 X17 12 20")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
