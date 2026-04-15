from EFA_v2 import *
def vsub_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-740968432, -1221865274, 1568249350, 30059485, 1941926884, -982633832, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2930")
    tran0.writeAction("slorii X19 X19 12 3024")
    tran0.writeAction("slorii X19 X19 8 198")
    tran0.writeAction("slorii X19 X19 12 3389")
    tran0.writeAction("slorii X19 X19 12 1464")
    tran0.writeAction("slorii X19 X19 8 16")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 28")
    tran0.writeAction("slorii X17 X17 12 2731")
    tran0.writeAction("slorii X17 X17 8 221")
    tran0.writeAction("slorii X17 X17 12 1495")
    tran0.writeAction("slorii X17 X17 12 2454")
    tran0.writeAction("slorii X17 X17 8 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3158")
    tran0.writeAction("slorii X18 X18 12 3634")
    tran0.writeAction("slorii X18 X18 8 152")
    tran0.writeAction("slorii X18 X18 12 1851")
    tran0.writeAction("slorii X18 X18 12 3955")
    tran0.writeAction("slorii X18 X18 8 228")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
