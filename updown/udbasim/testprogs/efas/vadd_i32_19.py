from EFA_v2 import *
def vadd_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-654640155, 421334079, -792523087, -1197589407, -1474366251, 767735930, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 401")
    tran0.writeAction("slorii X19 X19 12 3340")
    tran0.writeAction("slorii X19 X19 8 63")
    tran0.writeAction("slorii X19 X19 12 3471")
    tran0.writeAction("slorii X19 X19 12 2811")
    tran0.writeAction("slorii X19 X19 8 229")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2953")
    tran0.writeAction("slorii X17 X17 12 3644")
    tran0.writeAction("slorii X17 X17 8 97")
    tran0.writeAction("slorii X17 X17 12 3340")
    tran0.writeAction("slorii X17 X17 12 782")
    tran0.writeAction("slorii X17 X17 8 177")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 732")
    tran0.writeAction("slorii X18 X18 12 696")
    tran0.writeAction("slorii X18 X18 8 122")
    tran0.writeAction("slorii X18 X18 12 2689")
    tran0.writeAction("slorii X18 X18 12 3828")
    tran0.writeAction("slorii X18 X18 8 213")
    tran0.writeAction("vadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
