from EFA_v2 import *
def vadd_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1741871690, -1369229259, -1055083164, -1976694493, 1983201564, 1498619446, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2790")
    tran0.writeAction("slorii X19 X19 12 824")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("slorii X19 X19 12 2434")
    tran0.writeAction("slorii X19 X19 12 3365")
    tran0.writeAction("slorii X19 X19 8 182")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2210")
    tran0.writeAction("slorii X17 X17 12 3593")
    tran0.writeAction("slorii X17 X17 8 35")
    tran0.writeAction("slorii X17 X17 12 3089")
    tran0.writeAction("slorii X17 X17 12 3253")
    tran0.writeAction("slorii X17 X17 8 100")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1429")
    tran0.writeAction("slorii X18 X18 12 798")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("slorii X18 X18 12 1891")
    tran0.writeAction("slorii X18 X18 12 1345")
    tran0.writeAction("slorii X18 X18 8 28")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
