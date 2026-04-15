from EFA_v2 import *
def hash_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3550137192287889446, 9047485856740116288]
    tran0.writeAction("movir X16 12612")
    tran0.writeAction("slorii X16 X16 12 2543")
    tran0.writeAction("slorii X16 X16 12 1930")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("movir X17 32143")
    tran0.writeAction("slorii X17 X17 12 519")
    tran0.writeAction("slorii X17 X17 12 889")
    tran0.writeAction("slorii X17 X17 12 1496")
    tran0.writeAction("slorii X17 X17 12 1856")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
