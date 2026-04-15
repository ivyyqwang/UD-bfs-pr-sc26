from EFA_v2 import *
def vdiv_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [713149591, 2021094657, -213459848, 37643193, 815489285, 700270974, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1927")
    tran0.writeAction("slorii X19 X19 12 1909")
    tran0.writeAction("slorii X19 X19 8 1")
    tran0.writeAction("slorii X19 X19 12 680")
    tran0.writeAction("slorii X19 X19 12 460")
    tran0.writeAction("slorii X19 X19 8 151")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 35")
    tran0.writeAction("slorii X17 X17 12 3683")
    tran0.writeAction("slorii X17 X17 8 185")
    tran0.writeAction("slorii X17 X17 12 3892")
    tran0.writeAction("slorii X17 X17 12 1756")
    tran0.writeAction("slorii X17 X17 8 120")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 667")
    tran0.writeAction("slorii X18 X18 12 3401")
    tran0.writeAction("slorii X18 X18 8 126")
    tran0.writeAction("slorii X18 X18 12 777")
    tran0.writeAction("slorii X18 X18 12 2913")
    tran0.writeAction("slorii X18 X18 8 5")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
