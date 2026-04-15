from EFA_v2 import *
def addi_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7035376284942365488, 27861]
    tran0.writeAction("movir X16 40541")
    tran0.writeAction("slorii X16 X16 12 1320")
    tran0.writeAction("slorii X16 X16 12 2874")
    tran0.writeAction("slorii X16 X16 12 3288")
    tran0.writeAction("slorii X16 X16 12 3280")
    tran0.writeAction("addi X16 X17 27861")
    tran0.writeAction("yieldt")
    return efa
