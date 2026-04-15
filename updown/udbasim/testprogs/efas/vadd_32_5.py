from EFA_v2 import *
def vadd_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3317183278, 2275090770, 3253788581, 736352738, 4173701800, 318466211, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2169")
    tran0.writeAction("slorii X19 X19 12 2849")
    tran0.writeAction("slorii X19 X19 8 82")
    tran0.writeAction("slorii X19 X19 12 3163")
    tran0.writeAction("slorii X19 X19 12 2099")
    tran0.writeAction("slorii X19 X19 8 46")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 702")
    tran0.writeAction("slorii X17 X17 12 985")
    tran0.writeAction("slorii X17 X17 8 226")
    tran0.writeAction("slorii X17 X17 12 3103")
    tran0.writeAction("slorii X17 X17 12 223")
    tran0.writeAction("slorii X17 X17 8 165")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 303")
    tran0.writeAction("slorii X18 X18 12 2920")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("slorii X18 X18 12 3980")
    tran0.writeAction("slorii X18 X18 12 1442")
    tran0.writeAction("slorii X18 X18 8 168")
    tran0.writeAction("vadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
