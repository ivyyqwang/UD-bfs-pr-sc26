from EFA_v2 import *
def hash_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5065662629896505097, -3440525174015991185]
    tran0.writeAction("movir X16 47539")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("slorii X16 X16 12 3417")
    tran0.writeAction("slorii X16 X16 12 195")
    tran0.writeAction("slorii X16 X16 12 2295")
    tran0.writeAction("movir X17 53312")
    tran0.writeAction("slorii X17 X17 12 3273")
    tran0.writeAction("slorii X17 X17 12 1337")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("slorii X17 X17 12 623")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
