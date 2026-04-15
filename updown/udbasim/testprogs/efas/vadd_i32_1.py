from EFA_v2 import *
def vadd_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1367830290, -255490830, -1896961573, -315335343, -561812987, 1854233143, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3852")
    tran0.writeAction("slorii X19 X19 12 1412")
    tran0.writeAction("slorii X19 X19 8 242")
    tran0.writeAction("slorii X19 X19 12 2791")
    tran0.writeAction("slorii X19 X19 12 2192")
    tran0.writeAction("slorii X19 X19 8 238")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3795")
    tran0.writeAction("slorii X17 X17 12 1117")
    tran0.writeAction("slorii X17 X17 8 81")
    tran0.writeAction("slorii X17 X17 12 2286")
    tran0.writeAction("slorii X17 X17 12 3753")
    tran0.writeAction("slorii X17 X17 8 219")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1768")
    tran0.writeAction("slorii X18 X18 12 1370")
    tran0.writeAction("slorii X18 X18 8 55")
    tran0.writeAction("slorii X18 X18 12 3560")
    tran0.writeAction("slorii X18 X18 12 874")
    tran0.writeAction("slorii X18 X18 8 5")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
