from EFA_v2 import *
def div_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [369892722627219738, -6989555952499365557]
    tran0.writeAction("movir X16 1314")
    tran0.writeAction("slorii X16 X16 12 503")
    tran0.writeAction("slorii X16 X16 12 2225")
    tran0.writeAction("slorii X16 X16 12 809")
    tran0.writeAction("slorii X16 X16 12 282")
    tran0.writeAction("movir X17 40704")
    tran0.writeAction("slorii X17 X17 12 446")
    tran0.writeAction("slorii X17 X17 12 1209")
    tran0.writeAction("slorii X17 X17 12 2286")
    tran0.writeAction("slorii X17 X17 12 2379")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
