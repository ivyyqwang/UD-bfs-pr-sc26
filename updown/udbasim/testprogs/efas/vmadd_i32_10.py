from EFA_v2 import *
def vmadd_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-999539467, -1011159616, 1828465045, 1718204362, -1011085364, 1553170549, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3131")
    tran0.writeAction("slorii X19 X19 12 2797")
    tran0.writeAction("slorii X19 X19 8 192")
    tran0.writeAction("slorii X19 X19 12 3142")
    tran0.writeAction("slorii X19 X19 12 3132")
    tran0.writeAction("slorii X19 X19 8 245")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1638")
    tran0.writeAction("slorii X17 X17 12 2487")
    tran0.writeAction("slorii X17 X17 8 202")
    tran0.writeAction("slorii X17 X17 12 1743")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 8 149")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1481")
    tran0.writeAction("slorii X18 X18 12 896")
    tran0.writeAction("slorii X18 X18 8 117")
    tran0.writeAction("slorii X18 X18 12 3131")
    tran0.writeAction("slorii X18 X18 12 3087")
    tran0.writeAction("slorii X18 X18 8 204")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
