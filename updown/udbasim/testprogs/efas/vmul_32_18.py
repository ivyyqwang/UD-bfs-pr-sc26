from EFA_v2 import *
def vmul_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [335664245, 1212070064, 4014716049, 901782707, 2333847745, 803151806, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1155")
    tran0.writeAction("slorii X19 X19 12 3768")
    tran0.writeAction("slorii X19 X19 8 176")
    tran0.writeAction("slorii X19 X19 12 320")
    tran0.writeAction("slorii X19 X19 12 468")
    tran0.writeAction("slorii X19 X19 8 117")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 860")
    tran0.writeAction("slorii X17 X17 12 28")
    tran0.writeAction("slorii X17 X17 8 179")
    tran0.writeAction("slorii X17 X17 12 3828")
    tran0.writeAction("slorii X17 X17 12 2996")
    tran0.writeAction("slorii X17 X17 8 145")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 765")
    tran0.writeAction("slorii X18 X18 12 3871")
    tran0.writeAction("slorii X18 X18 8 190")
    tran0.writeAction("slorii X18 X18 12 2225")
    tran0.writeAction("slorii X18 X18 12 2992")
    tran0.writeAction("slorii X18 X18 8 193")
    tran0.writeAction("vmul.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
