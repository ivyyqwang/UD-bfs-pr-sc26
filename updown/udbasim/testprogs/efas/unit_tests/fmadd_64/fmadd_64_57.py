from EFA_v2 import *
def fmadd_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11964258733602945937, 1940637806107089187, 2848168742645262648]
    tran0.writeAction("movir X16 42505")
    tran0.writeAction("slorii X16 X16 12 2398")
    tran0.writeAction("slorii X16 X16 12 3529")
    tran0.writeAction("slorii X16 X16 12 1099")
    tran0.writeAction("slorii X16 X16 12 2961")
    tran0.writeAction("movir X17 6894")
    tran0.writeAction("slorii X17 X17 12 2172")
    tran0.writeAction("slorii X17 X17 12 3454")
    tran0.writeAction("slorii X17 X17 12 2893")
    tran0.writeAction("slorii X17 X17 12 2339")
    tran0.writeAction("movir X18 10118")
    tran0.writeAction("slorii X18 X18 12 2982")
    tran0.writeAction("slorii X18 X18 12 405")
    tran0.writeAction("slorii X18 X18 12 3038")
    tran0.writeAction("slorii X18 X18 12 2360")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
