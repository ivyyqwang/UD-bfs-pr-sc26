from EFA_v2 import *
def vdiv_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [231973582, -1692738604, -482458296, 212564753, 1519631403, 1302117436, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2481")
    tran0.writeAction("slorii X19 X19 12 2779")
    tran0.writeAction("slorii X19 X19 8 212")
    tran0.writeAction("slorii X19 X19 12 221")
    tran0.writeAction("slorii X19 X19 12 930")
    tran0.writeAction("slorii X19 X19 8 206")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 202")
    tran0.writeAction("slorii X17 X17 12 2939")
    tran0.writeAction("slorii X17 X17 8 17")
    tran0.writeAction("slorii X17 X17 12 3635")
    tran0.writeAction("slorii X17 X17 12 3653")
    tran0.writeAction("slorii X17 X17 8 72")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1241")
    tran0.writeAction("slorii X18 X18 12 3260")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("slorii X18 X18 12 1449")
    tran0.writeAction("slorii X18 X18 12 956")
    tran0.writeAction("slorii X18 X18 8 43")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
