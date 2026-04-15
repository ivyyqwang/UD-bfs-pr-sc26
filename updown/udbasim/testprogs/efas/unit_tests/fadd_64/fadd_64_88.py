from EFA_v2 import *
def fadd_64_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6414935147525987211, 14366313425797249221]
    tran0.writeAction("movir X16 22790")
    tran0.writeAction("slorii X16 X16 12 1752")
    tran0.writeAction("slorii X16 X16 12 1893")
    tran0.writeAction("slorii X16 X16 12 1861")
    tran0.writeAction("slorii X16 X16 12 2955")
    tran0.writeAction("movir X17 51039")
    tran0.writeAction("slorii X17 X17 12 1631")
    tran0.writeAction("slorii X17 X17 12 476")
    tran0.writeAction("slorii X17 X17 12 2335")
    tran0.writeAction("slorii X17 X17 12 2245")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
