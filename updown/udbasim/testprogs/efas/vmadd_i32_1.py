from EFA_v2 import *
def vmadd_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-150823105, 1357675734, 434339847, 116603383, 1288621512, -1451022360, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1294")
    tran0.writeAction("slorii X19 X19 12 3196")
    tran0.writeAction("slorii X19 X19 8 214")
    tran0.writeAction("slorii X19 X19 12 3952")
    tran0.writeAction("slorii X19 X19 12 671")
    tran0.writeAction("slorii X19 X19 8 63")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 111")
    tran0.writeAction("slorii X17 X17 12 825")
    tran0.writeAction("slorii X17 X17 8 247")
    tran0.writeAction("slorii X17 X17 12 414")
    tran0.writeAction("slorii X17 X17 12 896")
    tran0.writeAction("slorii X17 X17 8 7")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2712")
    tran0.writeAction("slorii X18 X18 12 807")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("slorii X18 X18 12 1228")
    tran0.writeAction("slorii X18 X18 12 3789")
    tran0.writeAction("slorii X18 X18 8 200")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
