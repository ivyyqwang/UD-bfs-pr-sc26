from EFA_v2 import *
def fmadd_64_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18371612525423638042, 11308110309521024493, 15102221827872327556]
    tran0.writeAction("movir X16 65269")
    tran0.writeAction("slorii X16 X16 12 324")
    tran0.writeAction("slorii X16 X16 12 320")
    tran0.writeAction("slorii X16 X16 12 4067")
    tran0.writeAction("slorii X16 X16 12 1562")
    tran0.writeAction("movir X17 40174")
    tran0.writeAction("slorii X17 X17 12 1958")
    tran0.writeAction("slorii X17 X17 12 2527")
    tran0.writeAction("slorii X17 X17 12 3822")
    tran0.writeAction("slorii X17 X17 12 1517")
    tran0.writeAction("movir X18 53653")
    tran0.writeAction("slorii X18 X18 12 3563")
    tran0.writeAction("slorii X18 X18 12 3273")
    tran0.writeAction("slorii X18 X18 12 1968")
    tran0.writeAction("slorii X18 X18 12 1924")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
