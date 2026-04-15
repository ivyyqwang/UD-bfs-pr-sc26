from EFA_v2 import *
def fmadd_32_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3650357820, 1388231722, 2398026086]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 217")
    tran0.writeAction("slorii X16 X16 12 2368")
    tran0.writeAction("slorii X16 X16 12 2620")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 82")
    tran0.writeAction("slorii X17 X17 12 3051")
    tran0.writeAction("slorii X17 X17 12 3114")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 142")
    tran0.writeAction("slorii X18 X18 12 3823")
    tran0.writeAction("slorii X18 X18 12 2406")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
