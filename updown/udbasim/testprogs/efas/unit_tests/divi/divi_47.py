from EFA_v2 import *
def divi_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5240999421534538052, 23115]
    tran0.writeAction("movir X16 46916")
    tran0.writeAction("slorii X16 X16 12 940")
    tran0.writeAction("slorii X16 X16 12 2891")
    tran0.writeAction("slorii X16 X16 12 1663")
    tran0.writeAction("slorii X16 X16 12 1724")
    tran0.writeAction("divi X16 X17 23115")
    tran0.writeAction("yieldt")
    return efa
