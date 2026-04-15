from EFA_v2 import *
def add_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5596473455609242842, 6008255086607795205]
    tran0.writeAction("movir X16 19882")
    tran0.writeAction("slorii X16 X16 12 2735")
    tran0.writeAction("slorii X16 X16 12 1244")
    tran0.writeAction("slorii X16 X16 12 2014")
    tran0.writeAction("slorii X16 X16 12 1242")
    tran0.writeAction("movir X17 21345")
    tran0.writeAction("slorii X17 X17 12 2498")
    tran0.writeAction("slorii X17 X17 12 2829")
    tran0.writeAction("slorii X17 X17 12 784")
    tran0.writeAction("slorii X17 X17 12 1029")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
