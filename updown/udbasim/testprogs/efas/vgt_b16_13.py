from EFA_v2 import *
def vgt_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [50973, 12501, 32172, 10829, 7251, 926, 4516, 64852, 32936, 38384, 35387, 6354, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 676")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2010")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 781")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 3185")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4053")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 282")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 57")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 453")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 397")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2211")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2399")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2058")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vgt.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
