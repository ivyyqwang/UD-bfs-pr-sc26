from EFA_v2 import *
def vdiv_b16_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4890, 18133, 35517, 59298, 51426, 56793, 24169, 16206, 4803, 50937, 28046, 18021, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3706")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 2219")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 1133")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 305")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1012")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 1510")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3549")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3214")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1126")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1752")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3183")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 300")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vdiv.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
