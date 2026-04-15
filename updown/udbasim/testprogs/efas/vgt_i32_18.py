from EFA_v2 import *
def vgt_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [983944147, -1726270399, 653183718, 424841089, 1151089479, -558705699, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2449")
    tran0.writeAction("slorii X19 X19 12 2868")
    tran0.writeAction("slorii X19 X19 8 65")
    tran0.writeAction("slorii X19 X19 12 938")
    tran0.writeAction("slorii X19 X19 12 1483")
    tran0.writeAction("slorii X19 X19 8 211")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 405")
    tran0.writeAction("slorii X17 X17 12 655")
    tran0.writeAction("slorii X17 X17 8 129")
    tran0.writeAction("slorii X17 X17 12 622")
    tran0.writeAction("slorii X17 X17 12 3786")
    tran0.writeAction("slorii X17 X17 8 230")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3563")
    tran0.writeAction("slorii X18 X18 12 723")
    tran0.writeAction("slorii X18 X18 8 221")
    tran0.writeAction("slorii X18 X18 12 1097")
    tran0.writeAction("slorii X18 X18 12 3131")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("vgt.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
