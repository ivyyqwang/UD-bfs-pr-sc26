from EFA_v2 import *
def vgt_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2735413985, 2099307644, 3130543428, 3800299992, 2661059725, 2373870147, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2002")
    tran0.writeAction("slorii X19 X19 12 228")
    tran0.writeAction("slorii X19 X19 8 124")
    tran0.writeAction("slorii X19 X19 12 2608")
    tran0.writeAction("slorii X19 X19 12 2842")
    tran0.writeAction("slorii X19 X19 8 225")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3624")
    tran0.writeAction("slorii X17 X17 12 1017")
    tran0.writeAction("slorii X17 X17 8 216")
    tran0.writeAction("slorii X17 X17 12 2985")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 8 68")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2263")
    tran0.writeAction("slorii X18 X18 12 3682")
    tran0.writeAction("slorii X18 X18 8 67")
    tran0.writeAction("slorii X18 X18 12 2537")
    tran0.writeAction("slorii X18 X18 12 3212")
    tran0.writeAction("slorii X18 X18 8 141")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
