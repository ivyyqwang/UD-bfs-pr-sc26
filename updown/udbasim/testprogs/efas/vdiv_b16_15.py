from EFA_v2 import *
def vdiv_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [42422, 23254, 40179, 36433, 26628, 5007, 30928, 63254, 38816, 34057, 629, 60860, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2277")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 2511")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1453")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2651")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3953")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1933")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 312")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 1664")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3803")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 39")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2128")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2426")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vdiv.b16 X19 X17 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
