from EFA_v2 import *
def fmadd_32_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3541324001, 1735974050, 272300116]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 211")
    tran0.writeAction("slorii X16 X16 12 325")
    tran0.writeAction("slorii X16 X16 12 225")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 103")
    tran0.writeAction("slorii X17 X17 12 1933")
    tran0.writeAction("slorii X17 X17 12 3234")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 16")
    tran0.writeAction("slorii X18 X18 12 943")
    tran0.writeAction("slorii X18 X18 12 2132")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
