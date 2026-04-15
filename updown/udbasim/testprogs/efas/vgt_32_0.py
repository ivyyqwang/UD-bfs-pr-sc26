from EFA_v2 import *
def vgt_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [876455737, 1308832715, 454912533, 1961115582, 3794732815, 2036377211, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1248")
    tran0.writeAction("slorii X19 X19 12 819")
    tran0.writeAction("slorii X19 X19 8 203")
    tran0.writeAction("slorii X19 X19 12 835")
    tran0.writeAction("slorii X19 X19 12 3495")
    tran0.writeAction("slorii X19 X19 8 57")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1870")
    tran0.writeAction("slorii X17 X17 12 1087")
    tran0.writeAction("slorii X17 X17 8 190")
    tran0.writeAction("slorii X17 X17 12 433")
    tran0.writeAction("slorii X17 X17 12 3434")
    tran0.writeAction("slorii X17 X17 8 21")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1942")
    tran0.writeAction("slorii X18 X18 12 166")
    tran0.writeAction("slorii X18 X18 8 123")
    tran0.writeAction("slorii X18 X18 12 3618")
    tran0.writeAction("slorii X18 X18 12 3847")
    tran0.writeAction("slorii X18 X18 8 15")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
