from EFA_v2 import *
def add_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2868971915064976342, 4639008587577761440]
    tran0.writeAction("movir X16 10192")
    tran0.writeAction("slorii X16 X16 12 2604")
    tran0.writeAction("slorii X16 X16 12 412")
    tran0.writeAction("slorii X16 X16 12 82")
    tran0.writeAction("slorii X16 X16 12 982")
    tran0.writeAction("movir X17 16481")
    tran0.writeAction("slorii X17 X17 12 283")
    tran0.writeAction("slorii X17 X17 12 2908")
    tran0.writeAction("slorii X17 X17 12 2289")
    tran0.writeAction("slorii X17 X17 12 3744")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
