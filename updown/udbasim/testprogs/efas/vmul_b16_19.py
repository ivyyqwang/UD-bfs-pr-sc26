from EFA_v2 import *
def vmul_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [21266, 50697, 13364, 7429, 55369, 10527, 58514, 23036, 38553, 36258, 24937, 455, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 464")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 835")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 3168")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1329")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1439")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 3657")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 657")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 3460")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 28")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1558")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2266")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2409")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vmul.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
