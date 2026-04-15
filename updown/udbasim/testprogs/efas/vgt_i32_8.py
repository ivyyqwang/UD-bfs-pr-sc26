from EFA_v2 import *
def vgt_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [219043389, -410561239, 2094386168, -1119421499, -1506114209, -889277603, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3704")
    tran0.writeAction("slorii X19 X19 12 1877")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("slorii X19 X19 12 208")
    tran0.writeAction("slorii X19 X19 12 3670")
    tran0.writeAction("slorii X19 X19 8 61")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3028")
    tran0.writeAction("slorii X17 X17 12 1787")
    tran0.writeAction("slorii X17 X17 8 197")
    tran0.writeAction("slorii X17 X17 12 1997")
    tran0.writeAction("slorii X17 X17 12 1483")
    tran0.writeAction("slorii X17 X17 8 248")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3247")
    tran0.writeAction("slorii X18 X18 12 3763")
    tran0.writeAction("slorii X18 X18 8 93")
    tran0.writeAction("slorii X18 X18 12 2659")
    tran0.writeAction("slorii X18 X18 12 2693")
    tran0.writeAction("slorii X18 X18 8 95")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
