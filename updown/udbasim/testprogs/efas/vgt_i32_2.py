from EFA_v2 import *
def vgt_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1104811397, -1832926988, 751785866, 1370659316, -866064959, 148567189, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2347")
    tran0.writeAction("slorii X19 X19 12 4032")
    tran0.writeAction("slorii X19 X19 8 244")
    tran0.writeAction("slorii X19 X19 12 1053")
    tran0.writeAction("slorii X19 X19 12 2581")
    tran0.writeAction("slorii X19 X19 8 133")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1307")
    tran0.writeAction("slorii X17 X17 12 665")
    tran0.writeAction("slorii X17 X17 8 244")
    tran0.writeAction("slorii X17 X17 12 716")
    tran0.writeAction("slorii X17 X17 12 3927")
    tran0.writeAction("slorii X17 X17 8 138")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 141")
    tran0.writeAction("slorii X18 X18 12 2804")
    tran0.writeAction("slorii X18 X18 8 149")
    tran0.writeAction("slorii X18 X18 12 3270")
    tran0.writeAction("slorii X18 X18 12 229")
    tran0.writeAction("slorii X18 X18 8 193")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
