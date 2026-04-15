from EFA_v2 import *
def vgt_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1905780059, 460393126, -455024673, 929685834, 417545056, 1428381770, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 439")
    tran0.writeAction("slorii X19 X19 12 266")
    tran0.writeAction("slorii X19 X19 8 166")
    tran0.writeAction("slorii X19 X19 12 1817")
    tran0.writeAction("slorii X19 X19 12 2021")
    tran0.writeAction("slorii X19 X19 8 91")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 886")
    tran0.writeAction("slorii X17 X17 12 2529")
    tran0.writeAction("slorii X17 X17 8 74")
    tran0.writeAction("slorii X17 X17 12 3662")
    tran0.writeAction("slorii X17 X17 12 223")
    tran0.writeAction("slorii X17 X17 8 223")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1362")
    tran0.writeAction("slorii X18 X18 12 864")
    tran0.writeAction("slorii X18 X18 8 74")
    tran0.writeAction("slorii X18 X18 12 398")
    tran0.writeAction("slorii X18 X18 12 827")
    tran0.writeAction("slorii X18 X18 8 96")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
