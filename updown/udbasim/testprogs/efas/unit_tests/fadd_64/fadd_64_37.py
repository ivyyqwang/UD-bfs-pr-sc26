from EFA_v2 import *
def fadd_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18286400746925443618, 7574548184751091157]
    tran0.writeAction("movir X16 64966")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 3804")
    tran0.writeAction("slorii X16 X16 12 2594")
    tran0.writeAction("movir X17 26910")
    tran0.writeAction("slorii X17 X17 12 823")
    tran0.writeAction("slorii X17 X17 12 318")
    tran0.writeAction("slorii X17 X17 12 690")
    tran0.writeAction("slorii X17 X17 12 3541")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
