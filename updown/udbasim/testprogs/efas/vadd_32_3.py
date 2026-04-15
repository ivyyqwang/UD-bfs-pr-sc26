from EFA_v2 import *
def vadd_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2124928482, 2466084345, 3289274838, 3034875375, 3621415183, 245920037, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2351")
    tran0.writeAction("slorii X19 X19 12 3445")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("slorii X19 X19 12 2026")
    tran0.writeAction("slorii X19 X19 12 2005")
    tran0.writeAction("slorii X19 X19 8 226")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2894")
    tran0.writeAction("slorii X17 X17 12 1157")
    tran0.writeAction("slorii X17 X17 8 239")
    tran0.writeAction("slorii X17 X17 12 3136")
    tran0.writeAction("slorii X17 X17 12 3673")
    tran0.writeAction("slorii X17 X17 8 214")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 234")
    tran0.writeAction("slorii X18 X18 12 2161")
    tran0.writeAction("slorii X18 X18 8 37")
    tran0.writeAction("slorii X18 X18 12 3453")
    tran0.writeAction("slorii X18 X18 12 2665")
    tran0.writeAction("slorii X18 X18 8 15")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
