from EFA_v2 import *
def vmul_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15896, 50778, 10523, 5992, 20413, 58689, 27287, 13839, 58550, 6265, 61392, 48383, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 374")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 657")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3173")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 993")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 864")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 1705")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3668")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 1275")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3023")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 3837")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 391")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3659")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vmul.b16 X19 X17 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
