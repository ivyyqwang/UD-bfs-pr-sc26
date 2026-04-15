from EFA_v2 import *
def vdiv_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1100067764, 1351458326, 599070796, 2530070774, 3709454032, 2938851851, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1288")
    tran0.writeAction("slorii X19 X19 12 3486")
    tran0.writeAction("slorii X19 X19 8 22")
    tran0.writeAction("slorii X19 X19 12 1049")
    tran0.writeAction("slorii X19 X19 12 435")
    tran0.writeAction("slorii X19 X19 8 180")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2412")
    tran0.writeAction("slorii X17 X17 12 3536")
    tran0.writeAction("slorii X17 X17 8 246")
    tran0.writeAction("slorii X17 X17 12 571")
    tran0.writeAction("slorii X17 X17 12 1304")
    tran0.writeAction("slorii X17 X17 8 76")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2802")
    tran0.writeAction("slorii X18 X18 12 2898")
    tran0.writeAction("slorii X18 X18 8 11")
    tran0.writeAction("slorii X18 X18 12 3537")
    tran0.writeAction("slorii X18 X18 12 2502")
    tran0.writeAction("slorii X18 X18 8 208")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
