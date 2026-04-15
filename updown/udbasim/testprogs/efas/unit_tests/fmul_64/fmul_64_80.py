from EFA_v2 import *
def fmul_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15635125764203068084, 9964185032888679074]
    tran0.writeAction("movir X16 55547")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 2889")
    tran0.writeAction("slorii X16 X16 12 3611")
    tran0.writeAction("slorii X16 X16 12 2740")
    tran0.writeAction("movir X17 35399")
    tran0.writeAction("slorii X17 X17 12 3671")
    tran0.writeAction("slorii X17 X17 12 3761")
    tran0.writeAction("slorii X17 X17 12 2431")
    tran0.writeAction("slorii X17 X17 12 2722")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
