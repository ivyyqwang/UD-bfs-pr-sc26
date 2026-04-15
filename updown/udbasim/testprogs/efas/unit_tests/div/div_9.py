from EFA_v2 import *
def div_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2634762685973873761, -3243270179988752859]
    tran0.writeAction("movir X16 9360")
    tran0.writeAction("slorii X16 X16 12 2283")
    tran0.writeAction("slorii X16 X16 12 1036")
    tran0.writeAction("slorii X16 X16 12 3796")
    tran0.writeAction("slorii X16 X16 12 1121")
    tran0.writeAction("movir X17 54013")
    tran0.writeAction("slorii X17 X17 12 2415")
    tran0.writeAction("slorii X17 X17 12 1139")
    tran0.writeAction("slorii X17 X17 12 627")
    tran0.writeAction("slorii X17 X17 12 1573")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
