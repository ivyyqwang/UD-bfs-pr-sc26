from EFA_v2 import *
def vsqrt_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-639583485, 1797201117, 86471857, 1511202144, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1713")
    tran0.writeAction("slorii X19 X19 12 3868")
    tran0.writeAction("slorii X19 X19 8 221")
    tran0.writeAction("slorii X19 X19 12 3486")
    tran0.writeAction("slorii X19 X19 12 187")
    tran0.writeAction("slorii X19 X19 8 3")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1441")
    tran0.writeAction("slorii X18 X18 12 797")
    tran0.writeAction("slorii X18 X18 8 96")
    tran0.writeAction("slorii X18 X18 12 82")
    tran0.writeAction("slorii X18 X18 12 1908")
    tran0.writeAction("slorii X18 X18 8 177")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
