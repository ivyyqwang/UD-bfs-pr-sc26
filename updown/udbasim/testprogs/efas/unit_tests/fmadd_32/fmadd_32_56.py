from EFA_v2 import *
def fmadd_32_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2196249307, 3035162247, 137979017]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 3713")
    tran0.writeAction("slorii X16 X16 12 2779")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 180")
    tran0.writeAction("slorii X17 X17 12 3726")
    tran0.writeAction("slorii X17 X17 12 1671")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 8")
    tran0.writeAction("slorii X18 X18 12 918")
    tran0.writeAction("slorii X18 X18 12 1161")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
