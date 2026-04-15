from EFA_v2 import *
def fmadd_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1568070176367918613, 9725370175799736803, 13306636981371292522]
    tran0.writeAction("movir X16 5570")
    tran0.writeAction("slorii X16 X16 12 3704")
    tran0.writeAction("slorii X16 X16 12 1141")
    tran0.writeAction("slorii X16 X16 12 1203")
    tran0.writeAction("slorii X16 X16 12 3605")
    tran0.writeAction("movir X17 34551")
    tran0.writeAction("slorii X17 X17 12 1866")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("slorii X17 X17 12 2955")
    tran0.writeAction("slorii X17 X17 12 2531")
    tran0.writeAction("movir X18 47274")
    tran0.writeAction("slorii X18 X18 12 2749")
    tran0.writeAction("slorii X18 X18 12 1341")
    tran0.writeAction("slorii X18 X18 12 2916")
    tran0.writeAction("slorii X18 X18 12 2922")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
