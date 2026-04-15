from EFA_v2 import *
def vsqrt_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [64202, 16761, 47381, 52315, 39458, 27420, 28067, 61651, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3269")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 2961")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 1047")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 4012")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3853")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1754")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1713")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2466")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("vsqrt.b16 X19 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
