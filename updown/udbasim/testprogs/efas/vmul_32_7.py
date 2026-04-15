from EFA_v2 import *
def vmul_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1233413764, 1199363209, 4239124945, 2805080609, 3023179330, 2975572182, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1143")
    tran0.writeAction("slorii X19 X19 12 3284")
    tran0.writeAction("slorii X19 X19 8 137")
    tran0.writeAction("slorii X19 X19 12 1176")
    tran0.writeAction("slorii X19 X19 12 1126")
    tran0.writeAction("slorii X19 X19 8 132")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2675")
    tran0.writeAction("slorii X17 X17 12 546")
    tran0.writeAction("slorii X17 X17 8 33")
    tran0.writeAction("slorii X17 X17 12 4042")
    tran0.writeAction("slorii X17 X17 12 3049")
    tran0.writeAction("slorii X17 X17 8 209")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2837")
    tran0.writeAction("slorii X18 X18 12 2976")
    tran0.writeAction("slorii X18 X18 8 214")
    tran0.writeAction("slorii X18 X18 12 2883")
    tran0.writeAction("slorii X18 X18 12 526")
    tran0.writeAction("slorii X18 X18 8 66")
    tran0.writeAction("vmul.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
