from EFA_v2 import *
def sub_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2050441097520969458, 2088884766958139553]
    tran0.writeAction("movir X16 7284")
    tran0.writeAction("slorii X16 X16 12 2581")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 2455")
    tran0.writeAction("slorii X16 X16 12 1778")
    tran0.writeAction("movir X17 7421")
    tran0.writeAction("slorii X17 X17 12 858")
    tran0.writeAction("slorii X17 X17 12 207")
    tran0.writeAction("slorii X17 X17 12 1083")
    tran0.writeAction("slorii X17 X17 12 2209")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
