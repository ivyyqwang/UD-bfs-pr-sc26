from EFA_v2 import *
def fmadd_32_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3106489890, 1756530923, 895610204]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 185")
    tran0.writeAction("slorii X16 X16 12 660")
    tran0.writeAction("slorii X16 X16 12 1570")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 104")
    tran0.writeAction("slorii X17 X17 12 2856")
    tran0.writeAction("slorii X17 X17 12 2283")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 53")
    tran0.writeAction("slorii X18 X18 12 1566")
    tran0.writeAction("slorii X18 X18 12 3420")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
