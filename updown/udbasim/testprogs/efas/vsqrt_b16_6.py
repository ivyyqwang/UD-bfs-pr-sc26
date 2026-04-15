from EFA_v2 import *
def vsqrt_b16_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [38798, 39622, 54974, 37454, 35103, 45051, 39976, 9237, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2340")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3435")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2476")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2424")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 577")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2498")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2815")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2193")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vsqrt.b16 X19 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
