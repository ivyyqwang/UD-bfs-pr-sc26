from EFA_v2 import *
def vsub_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1432173559, -1957241182, 468574579, 1137513127, 1420242853, 32275894, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2229")
    tran0.writeAction("slorii X19 X19 12 1758")
    tran0.writeAction("slorii X19 X19 8 162")
    tran0.writeAction("slorii X19 X19 12 1365")
    tran0.writeAction("slorii X19 X19 12 3387")
    tran0.writeAction("slorii X19 X19 8 247")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1084")
    tran0.writeAction("slorii X17 X17 12 3346")
    tran0.writeAction("slorii X17 X17 8 167")
    tran0.writeAction("slorii X17 X17 12 446")
    tran0.writeAction("slorii X17 X17 12 3553")
    tran0.writeAction("slorii X17 X17 8 115")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 30")
    tran0.writeAction("slorii X18 X18 12 3197")
    tran0.writeAction("slorii X18 X18 8 182")
    tran0.writeAction("slorii X18 X18 12 1354")
    tran0.writeAction("slorii X18 X18 12 1839")
    tran0.writeAction("slorii X18 X18 8 165")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
