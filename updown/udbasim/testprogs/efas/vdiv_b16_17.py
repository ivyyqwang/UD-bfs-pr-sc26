from EFA_v2 import *
def vdiv_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [22404, 9843, 45146, 12713, 23770, 36903, 5576, 17012, 8916, 12260, 62328, 34329, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 794")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2821")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 615")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1400")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1063")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 348")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 2306")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2145")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3895")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 766")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 557")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("vdiv.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
