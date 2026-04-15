from EFA_v2 import *
def vadd_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1792594899, -1122578537, 1151663471, 480118115, -1368260029, 1942853790, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3025")
    tran0.writeAction("slorii X19 X19 12 1743")
    tran0.writeAction("slorii X19 X19 8 151")
    tran0.writeAction("slorii X19 X19 12 1709")
    tran0.writeAction("slorii X19 X19 12 2259")
    tran0.writeAction("slorii X19 X19 8 211")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 457")
    tran0.writeAction("slorii X17 X17 12 3589")
    tran0.writeAction("slorii X17 X17 8 99")
    tran0.writeAction("slorii X17 X17 12 1098")
    tran0.writeAction("slorii X17 X17 12 1277")
    tran0.writeAction("slorii X17 X17 8 111")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1852")
    tran0.writeAction("slorii X18 X18 12 3480")
    tran0.writeAction("slorii X18 X18 8 158")
    tran0.writeAction("slorii X18 X18 12 2791")
    tran0.writeAction("slorii X18 X18 12 514")
    tran0.writeAction("slorii X18 X18 8 67")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
