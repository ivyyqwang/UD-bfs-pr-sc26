from EFA_v2 import *
def fmadd_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1866988828198694561, 2632435805404566607, 2982324057145240496]
    tran0.writeAction("movir X16 6632")
    tran0.writeAction("slorii X16 X16 12 3591")
    tran0.writeAction("slorii X16 X16 12 656")
    tran0.writeAction("slorii X16 X16 12 1662")
    tran0.writeAction("slorii X16 X16 12 3745")
    tran0.writeAction("movir X17 9352")
    tran0.writeAction("slorii X17 X17 12 1190")
    tran0.writeAction("slorii X17 X17 12 2803")
    tran0.writeAction("slorii X17 X17 12 649")
    tran0.writeAction("slorii X17 X17 12 1103")
    tran0.writeAction("movir X18 10595")
    tran0.writeAction("slorii X18 X18 12 1406")
    tran0.writeAction("slorii X18 X18 12 3535")
    tran0.writeAction("slorii X18 X18 12 998")
    tran0.writeAction("slorii X18 X18 12 2992")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
