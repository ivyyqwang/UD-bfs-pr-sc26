from EFA_v2 import *
def fmadd_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7204260904310279798, 2165481976636501267, 16716849159209330890]
    tran0.writeAction("movir X16 25594")
    tran0.writeAction("slorii X16 X16 12 2769")
    tran0.writeAction("slorii X16 X16 12 3942")
    tran0.writeAction("slorii X16 X16 12 2656")
    tran0.writeAction("slorii X16 X16 12 3702")
    tran0.writeAction("movir X17 7693")
    tran0.writeAction("slorii X17 X17 12 1382")
    tran0.writeAction("slorii X17 X17 12 624")
    tran0.writeAction("slorii X17 X17 12 3806")
    tran0.writeAction("slorii X17 X17 12 3347")
    tran0.writeAction("movir X18 59390")
    tran0.writeAction("slorii X18 X18 12 731")
    tran0.writeAction("slorii X18 X18 12 3482")
    tran0.writeAction("slorii X18 X18 12 1882")
    tran0.writeAction("slorii X18 X18 12 2250")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
