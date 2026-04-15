from EFA_v2 import *
def vdiv_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2114620096, 1284031171, 1188870615, 965672608, 1507403691, 1923922203, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1224")
    tran0.writeAction("slorii X19 X19 12 2242")
    tran0.writeAction("slorii X19 X19 8 195")
    tran0.writeAction("slorii X19 X19 12 2079")
    tran0.writeAction("slorii X19 X19 12 1397")
    tran0.writeAction("slorii X19 X19 8 64")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 920")
    tran0.writeAction("slorii X17 X17 12 3838")
    tran0.writeAction("slorii X17 X17 8 160")
    tran0.writeAction("slorii X17 X17 12 1133")
    tran0.writeAction("slorii X17 X17 12 3257")
    tran0.writeAction("slorii X17 X17 8 215")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1834")
    tran0.writeAction("slorii X18 X18 12 3257")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("slorii X18 X18 12 1437")
    tran0.writeAction("slorii X18 X18 12 2343")
    tran0.writeAction("slorii X18 X18 8 171")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
