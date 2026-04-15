from EFA_v2 import *
def fsub_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1531799749271483324, 14393227301037277084]
    tran0.writeAction("movir X16 5442")
    tran0.writeAction("slorii X16 X16 12 188")
    tran0.writeAction("slorii X16 X16 12 402")
    tran0.writeAction("slorii X16 X16 12 1471")
    tran0.writeAction("slorii X16 X16 12 956")
    tran0.writeAction("movir X17 51135")
    tran0.writeAction("slorii X17 X17 12 63")
    tran0.writeAction("slorii X17 X17 12 2241")
    tran0.writeAction("slorii X17 X17 12 3199")
    tran0.writeAction("slorii X17 X17 12 3996")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
