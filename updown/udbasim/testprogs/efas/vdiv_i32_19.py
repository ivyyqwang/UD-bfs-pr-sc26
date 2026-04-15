from EFA_v2 import *
def vdiv_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1869959138, -748818716, -1997069673, 1628964386, -2098443978, -1096613091, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3381")
    tran0.writeAction("slorii X19 X19 12 3566")
    tran0.writeAction("slorii X19 X19 8 228")
    tran0.writeAction("slorii X19 X19 12 1783")
    tran0.writeAction("slorii X19 X19 12 1359")
    tran0.writeAction("slorii X19 X19 8 226")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1553")
    tran0.writeAction("slorii X17 X17 12 2054")
    tran0.writeAction("slorii X17 X17 8 34")
    tran0.writeAction("slorii X17 X17 12 2191")
    tran0.writeAction("slorii X17 X17 12 1826")
    tran0.writeAction("slorii X17 X17 8 151")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3050")
    tran0.writeAction("slorii X18 X18 12 771")
    tran0.writeAction("slorii X18 X18 8 29")
    tran0.writeAction("slorii X18 X18 12 2094")
    tran0.writeAction("slorii X18 X18 12 3145")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("vdiv.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
