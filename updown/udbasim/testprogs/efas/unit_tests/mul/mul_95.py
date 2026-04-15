from EFA_v2 import *
def mul_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1773896492206441590, 4690483044603795895]
    tran0.writeAction("movir X16 6302")
    tran0.writeAction("slorii X16 X16 12 599")
    tran0.writeAction("slorii X16 X16 12 1550")
    tran0.writeAction("slorii X16 X16 12 1132")
    tran0.writeAction("slorii X16 X16 12 1142")
    tran0.writeAction("movir X17 16663")
    tran0.writeAction("slorii X17 X17 12 3863")
    tran0.writeAction("slorii X17 X17 12 2642")
    tran0.writeAction("slorii X17 X17 12 2465")
    tran0.writeAction("slorii X17 X17 12 2487")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
