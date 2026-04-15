from EFA_v2 import *
def vadd_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1933214935, 1704379467, 819823439, 1733597062, -1588473664, -743646012, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1625")
    tran0.writeAction("slorii X19 X19 12 1732")
    tran0.writeAction("slorii X19 X19 8 75")
    tran0.writeAction("slorii X19 X19 12 1843")
    tran0.writeAction("slorii X19 X19 12 2692")
    tran0.writeAction("slorii X19 X19 8 215")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1653")
    tran0.writeAction("slorii X17 X17 12 1175")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("slorii X17 X17 12 781")
    tran0.writeAction("slorii X17 X17 12 3459")
    tran0.writeAction("slorii X17 X17 8 79")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3386")
    tran0.writeAction("slorii X18 X18 12 3292")
    tran0.writeAction("slorii X18 X18 8 196")
    tran0.writeAction("slorii X18 X18 12 2581")
    tran0.writeAction("slorii X18 X18 12 464")
    tran0.writeAction("slorii X18 X18 8 192")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
