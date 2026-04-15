from EFA_v2 import *
def vadd_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4122043399, 4007945364, 2711908650, 3804207955, 1366645410, 2718420961, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3822")
    tran0.writeAction("slorii X19 X19 12 1124")
    tran0.writeAction("slorii X19 X19 8 148")
    tran0.writeAction("slorii X19 X19 12 3931")
    tran0.writeAction("slorii X19 X19 12 356")
    tran0.writeAction("slorii X19 X19 8 7")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3627")
    tran0.writeAction("slorii X17 X17 12 3995")
    tran0.writeAction("slorii X17 X17 8 83")
    tran0.writeAction("slorii X17 X17 12 2586")
    tran0.writeAction("slorii X17 X17 12 1137")
    tran0.writeAction("slorii X17 X17 8 42")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2592")
    tran0.writeAction("slorii X18 X18 12 1999")
    tran0.writeAction("slorii X18 X18 8 225")
    tran0.writeAction("slorii X18 X18 12 1303")
    tran0.writeAction("slorii X18 X18 12 1370")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
