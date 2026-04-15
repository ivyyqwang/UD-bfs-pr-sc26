from EFA_v2 import *
def vmul_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3657170090, 2407444040, 848593771, 3097761317, 4010078951, 3629219921, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2295")
    tran0.writeAction("slorii X19 X19 12 3758")
    tran0.writeAction("slorii X19 X19 8 72")
    tran0.writeAction("slorii X19 X19 12 3487")
    tran0.writeAction("slorii X19 X19 12 3068")
    tran0.writeAction("slorii X19 X19 8 170")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2954")
    tran0.writeAction("slorii X17 X17 12 1046")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("slorii X17 X17 12 809")
    tran0.writeAction("slorii X17 X17 12 1155")
    tran0.writeAction("slorii X17 X17 8 107")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3461")
    tran0.writeAction("slorii X18 X18 12 384")
    tran0.writeAction("slorii X18 X18 8 81")
    tran0.writeAction("slorii X18 X18 12 3824")
    tran0.writeAction("slorii X18 X18 12 1266")
    tran0.writeAction("slorii X18 X18 8 231")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
