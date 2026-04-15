from EFA_v2 import *
def vsub_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2690304303, 2806539915, 1796572492, 1642774031, 4164294591, 1111465513, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2676")
    tran0.writeAction("slorii X19 X19 12 2150")
    tran0.writeAction("slorii X19 X19 8 139")
    tran0.writeAction("slorii X19 X19 12 2565")
    tran0.writeAction("slorii X19 X19 12 2761")
    tran0.writeAction("slorii X19 X19 8 47")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1566")
    tran0.writeAction("slorii X17 X17 12 2750")
    tran0.writeAction("slorii X17 X17 8 15")
    tran0.writeAction("slorii X17 X17 12 1713")
    tran0.writeAction("slorii X17 X17 12 1413")
    tran0.writeAction("slorii X17 X17 8 76")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1059")
    tran0.writeAction("slorii X18 X18 12 3998")
    tran0.writeAction("slorii X18 X18 8 41")
    tran0.writeAction("slorii X18 X18 12 3971")
    tran0.writeAction("slorii X18 X18 12 1559")
    tran0.writeAction("slorii X18 X18 8 191")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
