from EFA_v2 import *
def vsqrt_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [291640643, -1347333213, 1229096306, 265136597, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2811")
    tran0.writeAction("slorii X19 X19 12 339")
    tran0.writeAction("slorii X19 X19 8 163")
    tran0.writeAction("slorii X19 X19 12 278")
    tran0.writeAction("slorii X19 X19 12 533")
    tran0.writeAction("slorii X19 X19 8 67")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 252")
    tran0.writeAction("slorii X18 X18 12 3497")
    tran0.writeAction("slorii X18 X18 8 213")
    tran0.writeAction("slorii X18 X18 12 1172")
    tran0.writeAction("slorii X18 X18 12 645")
    tran0.writeAction("slorii X18 X18 8 114")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
