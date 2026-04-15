from EFA_v2 import *
def vgt_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [22429, 4173, 9046, 29709, 42407, 58067, 29739, 10618, 10255, 53449, 29244, 57673, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1856")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 565")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 260")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 1401")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 663")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 1858")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 3629")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 2650")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3604")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1827")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 3340")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 640")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vgt.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
