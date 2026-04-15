from EFA_v2 import *
def vdiv_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-791471284, -687919307, 1427167393, -1425331579, -1330423340, -1616280979, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3439")
    tran0.writeAction("slorii X19 X19 12 3887")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("slorii X19 X19 12 3341")
    tran0.writeAction("slorii X19 X19 12 795")
    tran0.writeAction("slorii X19 X19 8 76")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2736")
    tran0.writeAction("slorii X17 X17 12 2858")
    tran0.writeAction("slorii X17 X17 8 133")
    tran0.writeAction("slorii X17 X17 12 1361")
    tran0.writeAction("slorii X17 X17 12 216")
    tran0.writeAction("slorii X17 X17 8 161")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2554")
    tran0.writeAction("slorii X18 X18 12 2434")
    tran0.writeAction("slorii X18 X18 8 109")
    tran0.writeAction("slorii X18 X18 12 2827")
    tran0.writeAction("slorii X18 X18 12 857")
    tran0.writeAction("slorii X18 X18 8 212")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
