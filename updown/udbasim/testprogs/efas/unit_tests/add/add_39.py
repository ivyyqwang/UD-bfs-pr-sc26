from EFA_v2 import *
def add_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8575164255390585307, 8208674402063965164]
    tran0.writeAction("movir X16 30465")
    tran0.writeAction("slorii X16 X16 12 423")
    tran0.writeAction("slorii X16 X16 12 1285")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("slorii X16 X16 12 475")
    tran0.writeAction("movir X17 29163")
    tran0.writeAction("slorii X17 X17 12 286")
    tran0.writeAction("slorii X17 X17 12 147")
    tran0.writeAction("slorii X17 X17 12 3541")
    tran0.writeAction("slorii X17 X17 12 3052")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
