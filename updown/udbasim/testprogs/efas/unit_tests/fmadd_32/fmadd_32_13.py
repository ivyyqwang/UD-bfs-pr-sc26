from EFA_v2 import *
def fmadd_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3665189682, 3301193264, 959006004]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 218")
    tran0.writeAction("slorii X16 X16 12 1893")
    tran0.writeAction("slorii X16 X16 12 2866")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 196")
    tran0.writeAction("slorii X17 X17 12 3139")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 57")
    tran0.writeAction("slorii X18 X18 12 660")
    tran0.writeAction("slorii X18 X18 12 1332")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
