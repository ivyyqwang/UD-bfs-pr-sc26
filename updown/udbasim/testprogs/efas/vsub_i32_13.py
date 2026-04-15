from EFA_v2 import *
def vsub_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1542341561, -552071410, 2022524390, 1538087855, -1038377260, -1982557967, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3569")
    tran0.writeAction("slorii X19 X19 12 2063")
    tran0.writeAction("slorii X19 X19 8 14")
    tran0.writeAction("slorii X19 X19 12 2625")
    tran0.writeAction("slorii X19 X19 12 444")
    tran0.writeAction("slorii X19 X19 8 71")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1466")
    tran0.writeAction("slorii X17 X17 12 3419")
    tran0.writeAction("slorii X17 X17 8 175")
    tran0.writeAction("slorii X17 X17 12 1928")
    tran0.writeAction("slorii X17 X17 12 3397")
    tran0.writeAction("slorii X17 X17 8 230")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2205")
    tran0.writeAction("slorii X18 X18 12 1168")
    tran0.writeAction("slorii X18 X18 8 241")
    tran0.writeAction("slorii X18 X18 12 3105")
    tran0.writeAction("slorii X18 X18 12 2974")
    tran0.writeAction("slorii X18 X18 8 212")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
