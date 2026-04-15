from EFA_v2 import *
def addi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2673464324777763187, 4341]
    tran0.writeAction("movir X16 56037")
    tran0.writeAction("slorii X16 X16 12 3877")
    tran0.writeAction("slorii X16 X16 12 3193")
    tran0.writeAction("slorii X16 X16 12 3857")
    tran0.writeAction("slorii X16 X16 12 3725")
    tran0.writeAction("addi X16 X17 4341")
    tran0.writeAction("yieldt")
    return efa
