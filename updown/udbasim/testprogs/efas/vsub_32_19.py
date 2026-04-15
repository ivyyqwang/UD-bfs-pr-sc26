from EFA_v2 import *
def vsub_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1233493134, 642118714, 2877621638, 2267870133, 3960960464, 2177280798, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 612")
    tran0.writeAction("slorii X19 X19 12 1524")
    tran0.writeAction("slorii X19 X19 8 58")
    tran0.writeAction("slorii X19 X19 12 1176")
    tran0.writeAction("slorii X19 X19 12 1436")
    tran0.writeAction("slorii X19 X19 8 142")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2162")
    tran0.writeAction("slorii X17 X17 12 3315")
    tran0.writeAction("slorii X17 X17 8 181")
    tran0.writeAction("slorii X17 X17 12 2744")
    tran0.writeAction("slorii X17 X17 12 1285")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2076")
    tran0.writeAction("slorii X18 X18 12 1707")
    tran0.writeAction("slorii X18 X18 8 30")
    tran0.writeAction("slorii X18 X18 12 3777")
    tran0.writeAction("slorii X18 X18 12 1909")
    tran0.writeAction("slorii X18 X18 8 208")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
