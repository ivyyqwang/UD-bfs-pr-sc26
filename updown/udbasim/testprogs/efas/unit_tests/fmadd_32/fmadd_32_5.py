from EFA_v2 import *
def fmadd_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [297457998, 3700257595, 3785744064]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 17")
    tran0.writeAction("slorii X16 X16 12 2989")
    tran0.writeAction("slorii X16 X16 12 2382")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 220")
    tran0.writeAction("slorii X17 X17 12 2263")
    tran0.writeAction("slorii X17 X17 12 827")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 225")
    tran0.writeAction("slorii X18 X18 12 2653")
    tran0.writeAction("slorii X18 X18 12 3776")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
