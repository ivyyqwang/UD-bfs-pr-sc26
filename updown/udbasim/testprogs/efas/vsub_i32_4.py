from EFA_v2 import *
def vsub_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [272638916, 1640223374, 1489757051, -1764232923, 636230959, -435466042, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1564")
    tran0.writeAction("slorii X19 X19 12 978")
    tran0.writeAction("slorii X19 X19 8 142")
    tran0.writeAction("slorii X19 X19 12 260")
    tran0.writeAction("slorii X19 X19 12 35")
    tran0.writeAction("slorii X19 X19 8 196")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2413")
    tran0.writeAction("slorii X17 X17 12 2033")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("slorii X17 X17 12 1420")
    tran0.writeAction("slorii X17 X17 12 3043")
    tran0.writeAction("slorii X17 X17 8 123")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3680")
    tran0.writeAction("slorii X18 X18 12 2896")
    tran0.writeAction("slorii X18 X18 8 198")
    tran0.writeAction("slorii X18 X18 12 606")
    tran0.writeAction("slorii X18 X18 12 3101")
    tran0.writeAction("slorii X18 X18 8 47")
    tran0.writeAction("vsub.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
