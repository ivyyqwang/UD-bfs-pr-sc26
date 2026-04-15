from EFA_v2 import *
def vmul_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3410272349, 1754034330, 1099868997, 2529081031, 1997807476, 615721266, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1672")
    tran0.writeAction("slorii X19 X19 12 3184")
    tran0.writeAction("slorii X19 X19 8 154")
    tran0.writeAction("slorii X19 X19 12 3252")
    tran0.writeAction("slorii X19 X19 12 1184")
    tran0.writeAction("slorii X19 X19 8 93")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2411")
    tran0.writeAction("slorii X17 X17 12 3766")
    tran0.writeAction("slorii X17 X17 8 199")
    tran0.writeAction("slorii X17 X17 12 1048")
    tran0.writeAction("slorii X17 X17 12 3755")
    tran0.writeAction("slorii X17 X17 8 69")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 587")
    tran0.writeAction("slorii X18 X18 12 809")
    tran0.writeAction("slorii X18 X18 8 50")
    tran0.writeAction("slorii X18 X18 12 1905")
    tran0.writeAction("slorii X18 X18 12 1055")
    tran0.writeAction("slorii X18 X18 8 116")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
