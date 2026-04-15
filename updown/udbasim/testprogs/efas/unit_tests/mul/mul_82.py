from EFA_v2 import *
def mul_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4086267206725227566, -9069824682797849254]
    tran0.writeAction("movir X16 51018")
    tran0.writeAction("slorii X16 X16 12 2714")
    tran0.writeAction("slorii X16 X16 12 29")
    tran0.writeAction("slorii X16 X16 12 3338")
    tran0.writeAction("slorii X16 X16 12 3026")
    tran0.writeAction("movir X17 33313")
    tran0.writeAction("slorii X17 X17 12 2088")
    tran0.writeAction("slorii X17 X17 12 326")
    tran0.writeAction("slorii X17 X17 12 3130")
    tran0.writeAction("slorii X17 X17 12 1370")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
