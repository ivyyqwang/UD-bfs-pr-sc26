from EFA_v2 import *
def vdiv_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1504040920, 4190886329, 2615919600, 4010543015, 1223893816, 31258894, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3996")
    tran0.writeAction("slorii X19 X19 12 3033")
    tran0.writeAction("slorii X19 X19 8 185")
    tran0.writeAction("slorii X19 X19 12 1434")
    tran0.writeAction("slorii X19 X19 12 1495")
    tran0.writeAction("slorii X19 X19 8 216")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3824")
    tran0.writeAction("slorii X17 X17 12 3079")
    tran0.writeAction("slorii X17 X17 8 167")
    tran0.writeAction("slorii X17 X17 12 2494")
    tran0.writeAction("slorii X17 X17 12 3011")
    tran0.writeAction("slorii X17 X17 8 240")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 29")
    tran0.writeAction("slorii X18 X18 12 3321")
    tran0.writeAction("slorii X18 X18 8 14")
    tran0.writeAction("slorii X18 X18 12 1167")
    tran0.writeAction("slorii X18 X18 12 803")
    tran0.writeAction("slorii X18 X18 8 56")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
