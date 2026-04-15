from EFA_v2 import *
def vgt_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [29804, 1962, 22505, 10353, 3646, 39499, 51437, 9420, 37178, 51770, 53493, 54643, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 647")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 1406")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 122")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 1862")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 588")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 3214")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 2468")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 227")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3415")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 3343")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 3235")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2323")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vgt.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
