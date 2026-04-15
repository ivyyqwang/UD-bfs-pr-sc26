from EFA_v2 import *
def vgt_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2163695742, 3232701138, 4012854596, 2287542714, 424496903, 1454250077, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3082")
    tran0.writeAction("slorii X19 X19 12 3866")
    tran0.writeAction("slorii X19 X19 8 210")
    tran0.writeAction("slorii X19 X19 12 2063")
    tran0.writeAction("slorii X19 X19 12 1888")
    tran0.writeAction("slorii X19 X19 8 126")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2181")
    tran0.writeAction("slorii X17 X17 12 2337")
    tran0.writeAction("slorii X17 X17 8 186")
    tran0.writeAction("slorii X17 X17 12 3826")
    tran0.writeAction("slorii X17 X17 12 3917")
    tran0.writeAction("slorii X17 X17 8 68")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1386")
    tran0.writeAction("slorii X18 X18 12 3608")
    tran0.writeAction("slorii X18 X18 8 93")
    tran0.writeAction("slorii X18 X18 12 404")
    tran0.writeAction("slorii X18 X18 12 3407")
    tran0.writeAction("slorii X18 X18 8 7")
    tran0.writeAction("vgt.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
