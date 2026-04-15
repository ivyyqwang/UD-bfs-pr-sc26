from EFA_v2 import *
def vgt_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12178212, -1826241346, 1527565617, 1480761478, 1132545763, 406813371, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2354")
    tran0.writeAction("slorii X19 X19 12 1476")
    tran0.writeAction("slorii X19 X19 8 190")
    tran0.writeAction("slorii X19 X19 12 11")
    tran0.writeAction("slorii X19 X19 12 2515")
    tran0.writeAction("slorii X19 X19 8 36")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1412")
    tran0.writeAction("slorii X17 X17 12 672")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("slorii X17 X17 12 1456")
    tran0.writeAction("slorii X17 X17 12 3277")
    tran0.writeAction("slorii X17 X17 8 49")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 387")
    tran0.writeAction("slorii X18 X18 12 3962")
    tran0.writeAction("slorii X18 X18 8 187")
    tran0.writeAction("slorii X18 X18 12 1080")
    tran0.writeAction("slorii X18 X18 12 326")
    tran0.writeAction("slorii X18 X18 8 227")
    tran0.writeAction("vgt.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
