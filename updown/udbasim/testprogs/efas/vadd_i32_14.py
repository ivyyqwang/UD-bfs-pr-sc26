from EFA_v2 import *
def vadd_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-380402443, -885882375, -712337968, 598748870, -381244368, -1340602093, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3251")
    tran0.writeAction("slorii X19 X19 12 641")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("slorii X19 X19 12 3733")
    tran0.writeAction("slorii X19 X19 12 900")
    tran0.writeAction("slorii X19 X19 8 245")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 571")
    tran0.writeAction("slorii X17 X17 12 46")
    tran0.writeAction("slorii X17 X17 8 198")
    tran0.writeAction("slorii X17 X17 12 3416")
    tran0.writeAction("slorii X17 X17 12 2709")
    tran0.writeAction("slorii X17 X17 8 208")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2817")
    tran0.writeAction("slorii X18 X18 12 2057")
    tran0.writeAction("slorii X18 X18 8 19")
    tran0.writeAction("slorii X18 X18 12 3732")
    tran0.writeAction("slorii X18 X18 12 1708")
    tran0.writeAction("slorii X18 X18 8 48")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
