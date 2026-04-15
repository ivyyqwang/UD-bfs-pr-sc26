from EFA_v2 import *
def vmadd_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1716976343, -1271828293, 2066073710, 1076899923, -1058807944, 1907295907, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2883")
    tran0.writeAction("slorii X19 X19 12 368")
    tran0.writeAction("slorii X19 X19 8 187")
    tran0.writeAction("slorii X19 X19 12 2458")
    tran0.writeAction("slorii X19 X19 12 2309")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1027")
    tran0.writeAction("slorii X17 X17 12 48")
    tran0.writeAction("slorii X17 X17 8 83")
    tran0.writeAction("slorii X17 X17 12 1970")
    tran0.writeAction("slorii X17 X17 12 1480")
    tran0.writeAction("slorii X17 X17 8 110")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1818")
    tran0.writeAction("slorii X18 X18 12 3846")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("slorii X18 X18 12 3086")
    tran0.writeAction("slorii X18 X18 12 991")
    tran0.writeAction("slorii X18 X18 8 120")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
