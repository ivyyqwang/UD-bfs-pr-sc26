from EFA_v2 import *
def vsqrt_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [23588, 61604, 13857, 36142, 56370, 29584, 10585, 64744, 4]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2258")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 866")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 3850")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1474")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4046")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 661")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1849")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3523")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("vsqrt.b16 X19 X18 4 ")
    tran0.writeAction("yieldt")
    return efa
