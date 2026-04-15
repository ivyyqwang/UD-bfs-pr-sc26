from EFA_v2 import *
def fmadd_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15669762988553716771, 15373232165431678068, 13555845226760944176]
    tran0.writeAction("movir X16 55670")
    tran0.writeAction("slorii X16 X16 12 742")
    tran0.writeAction("slorii X16 X16 12 2695")
    tran0.writeAction("slorii X16 X16 12 1260")
    tran0.writeAction("slorii X16 X16 12 1059")
    tran0.writeAction("movir X17 54616")
    tran0.writeAction("slorii X17 X17 12 2835")
    tran0.writeAction("slorii X17 X17 12 1054")
    tran0.writeAction("slorii X17 X17 12 673")
    tran0.writeAction("slorii X17 X17 12 1140")
    tran0.writeAction("movir X18 48160")
    tran0.writeAction("slorii X18 X18 12 150")
    tran0.writeAction("slorii X18 X18 12 2411")
    tran0.writeAction("slorii X18 X18 12 1067")
    tran0.writeAction("slorii X18 X18 12 2608")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
