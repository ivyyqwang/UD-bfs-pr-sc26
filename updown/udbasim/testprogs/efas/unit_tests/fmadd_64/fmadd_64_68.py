from EFA_v2 import *
def fmadd_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14376256893020913241, 10988536713747712886, 1725928023325921873]
    tran0.writeAction("movir X16 51074")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 2492")
    tran0.writeAction("slorii X16 X16 12 1115")
    tran0.writeAction("slorii X16 X16 12 3673")
    tran0.writeAction("movir X17 39039")
    tran0.writeAction("slorii X17 X17 12 510")
    tran0.writeAction("slorii X17 X17 12 3040")
    tran0.writeAction("slorii X17 X17 12 1108")
    tran0.writeAction("slorii X17 X17 12 2934")
    tran0.writeAction("movir X18 6131")
    tran0.writeAction("slorii X18 X18 12 2982")
    tran0.writeAction("slorii X18 X18 12 1170")
    tran0.writeAction("slorii X18 X18 12 957")
    tran0.writeAction("slorii X18 X18 12 593")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
