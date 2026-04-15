from EFA_v2 import *
def muli_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9067323700633653060, -8646]
    tran0.writeAction("movir X16 32213")
    tran0.writeAction("slorii X16 X16 12 2477")
    tran0.writeAction("slorii X16 X16 12 3439")
    tran0.writeAction("slorii X16 X16 12 3068")
    tran0.writeAction("slorii X16 X16 12 3908")
    tran0.writeAction("muli X16 X17 -8646")
    tran0.writeAction("yieldt")
    return efa
