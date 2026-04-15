from EFA_v2 import *
def vgt_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2150304748, 2756463046, 1096537690, 2481503160, 1219108012, 919896136, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2628")
    tran0.writeAction("slorii X19 X19 12 3145")
    tran0.writeAction("slorii X19 X19 8 198")
    tran0.writeAction("slorii X19 X19 12 2050")
    tran0.writeAction("slorii X19 X19 12 2827")
    tran0.writeAction("slorii X19 X19 8 236")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2366")
    tran0.writeAction("slorii X17 X17 12 2235")
    tran0.writeAction("slorii X17 X17 8 184")
    tran0.writeAction("slorii X17 X17 12 1045")
    tran0.writeAction("slorii X17 X17 12 3030")
    tran0.writeAction("slorii X17 X17 8 90")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 877")
    tran0.writeAction("slorii X18 X18 12 1152")
    tran0.writeAction("slorii X18 X18 8 72")
    tran0.writeAction("slorii X18 X18 12 1162")
    tran0.writeAction("slorii X18 X18 12 2588")
    tran0.writeAction("slorii X18 X18 8 172")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
