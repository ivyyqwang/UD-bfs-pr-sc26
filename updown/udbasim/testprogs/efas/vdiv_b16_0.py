from EFA_v2 import *
def vdiv_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10490, 20196, 51649, 61612, 64436, 60294, 7551, 36589, 22367, 1175, 39334, 23285, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3850")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 3228")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 1262")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 655")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2286")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 471")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 3768")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 4027")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1455")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2458")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 73")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1397")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vdiv.b16 X19 X17 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
