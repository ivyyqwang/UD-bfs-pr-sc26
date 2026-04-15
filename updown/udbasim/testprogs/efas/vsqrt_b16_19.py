from EFA_v2 import *
def vsqrt_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [55136, 48937, 55706, 36953, 2942, 55568, 40944, 39241, 9]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2309")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3481")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 3058")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3446")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2452")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2559")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3473")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 183")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("vsqrt.b16 X19 X18 9 ")
    tran0.writeAction("yieldt")
    return efa
