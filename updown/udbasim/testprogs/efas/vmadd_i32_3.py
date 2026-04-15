from EFA_v2 import *
def vmadd_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1297119785, 270538364, 1891224189, 279727915, -1798999230, -2098459871, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 258")
    tran0.writeAction("slorii X19 X19 12 22")
    tran0.writeAction("slorii X19 X19 8 124")
    tran0.writeAction("slorii X19 X19 12 1237")
    tran0.writeAction("slorii X19 X19 12 122")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 266")
    tran0.writeAction("slorii X17 X17 12 3151")
    tran0.writeAction("slorii X17 X17 8 43")
    tran0.writeAction("slorii X17 X17 12 1803")
    tran0.writeAction("slorii X17 X17 12 2506")
    tran0.writeAction("slorii X17 X17 8 125")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2094")
    tran0.writeAction("slorii X18 X18 12 3083")
    tran0.writeAction("slorii X18 X18 8 33")
    tran0.writeAction("slorii X18 X18 12 2380")
    tran0.writeAction("slorii X18 X18 12 1395")
    tran0.writeAction("slorii X18 X18 8 66")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
