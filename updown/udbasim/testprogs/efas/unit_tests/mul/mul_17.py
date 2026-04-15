from EFA_v2 import *
def mul_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6812419808929002698, -3476323681332616823]
    tran0.writeAction("movir X16 41333")
    tran0.writeAction("slorii X16 X16 12 1732")
    tran0.writeAction("slorii X16 X16 12 1803")
    tran0.writeAction("slorii X16 X16 12 3900")
    tran0.writeAction("slorii X16 X16 12 2870")
    tran0.writeAction("movir X17 53185")
    tran0.writeAction("slorii X17 X17 12 2528")
    tran0.writeAction("slorii X17 X17 12 1977")
    tran0.writeAction("slorii X17 X17 12 3650")
    tran0.writeAction("slorii X17 X17 12 393")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
