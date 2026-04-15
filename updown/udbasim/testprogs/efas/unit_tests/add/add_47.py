from EFA_v2 import *
def add_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [608473347892319443, 5032020877318262460]
    tran0.writeAction("movir X16 2161")
    tran0.writeAction("slorii X16 X16 12 2996")
    tran0.writeAction("slorii X16 X16 12 2364")
    tran0.writeAction("slorii X16 X16 12 1697")
    tran0.writeAction("slorii X16 X16 12 1235")
    tran0.writeAction("movir X17 17877")
    tran0.writeAction("slorii X17 X17 12 1349")
    tran0.writeAction("slorii X17 X17 12 958")
    tran0.writeAction("slorii X17 X17 12 3704")
    tran0.writeAction("slorii X17 X17 12 3772")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
