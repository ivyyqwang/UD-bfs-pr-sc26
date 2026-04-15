from EFA_v2 import *
def fmadd_64_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9282166881739012716, 13706019309308906318, 14744183688584087446]
    tran0.writeAction("movir X16 32976")
    tran0.writeAction("slorii X16 X16 12 3609")
    tran0.writeAction("slorii X16 X16 12 2451")
    tran0.writeAction("slorii X16 X16 12 3887")
    tran0.writeAction("slorii X16 X16 12 2668")
    tran0.writeAction("movir X17 48693")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("slorii X17 X17 12 440")
    tran0.writeAction("slorii X17 X17 12 8")
    tran0.writeAction("slorii X17 X17 12 2894")
    tran0.writeAction("movir X18 52381")
    tran0.writeAction("slorii X18 X18 12 3535")
    tran0.writeAction("slorii X18 X18 12 605")
    tran0.writeAction("slorii X18 X18 12 668")
    tran0.writeAction("slorii X18 X18 12 1942")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
