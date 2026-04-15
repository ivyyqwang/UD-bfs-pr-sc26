from EFA_v2 import *
def vmul_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3043225339, 1977473735, 4076165947, 1919019148, 205953321, 3115417479, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1885")
    tran0.writeAction("slorii X19 X19 12 3546")
    tran0.writeAction("slorii X19 X19 8 199")
    tran0.writeAction("slorii X19 X19 12 2902")
    tran0.writeAction("slorii X19 X19 12 1006")
    tran0.writeAction("slorii X19 X19 8 251")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1830")
    tran0.writeAction("slorii X17 X17 12 488")
    tran0.writeAction("slorii X17 X17 8 140")
    tran0.writeAction("slorii X17 X17 12 3887")
    tran0.writeAction("slorii X17 X17 12 1371")
    tran0.writeAction("slorii X17 X17 8 59")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2971")
    tran0.writeAction("slorii X18 X18 12 383")
    tran0.writeAction("slorii X18 X18 8 135")
    tran0.writeAction("slorii X18 X18 12 196")
    tran0.writeAction("slorii X18 X18 12 1689")
    tran0.writeAction("slorii X18 X18 8 41")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
