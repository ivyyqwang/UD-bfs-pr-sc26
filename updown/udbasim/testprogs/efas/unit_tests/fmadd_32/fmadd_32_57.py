from EFA_v2 import *
def fmadd_32_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1741113169, 3195081583, 4105531987]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 103")
    tran0.writeAction("slorii X16 X16 12 3188")
    tran0.writeAction("slorii X16 X16 12 1873")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 190")
    tran0.writeAction("slorii X17 X17 12 1809")
    tran0.writeAction("slorii X17 X17 12 879")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 244")
    tran0.writeAction("slorii X18 X18 12 2903")
    tran0.writeAction("slorii X18 X18 12 595")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
