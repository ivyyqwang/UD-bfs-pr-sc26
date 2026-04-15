from EFA_v2 import *
def vdiv_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1328664636, 585133756, 1658435385, 184888246, 4246448707, 948023801, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 558")
    tran0.writeAction("slorii X19 X19 12 110")
    tran0.writeAction("slorii X19 X19 8 188")
    tran0.writeAction("slorii X19 X19 12 1267")
    tran0.writeAction("slorii X19 X19 12 464")
    tran0.writeAction("slorii X19 X19 8 60")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 176")
    tran0.writeAction("slorii X17 X17 12 1323")
    tran0.writeAction("slorii X17 X17 8 182")
    tran0.writeAction("slorii X17 X17 12 1581")
    tran0.writeAction("slorii X17 X17 12 2487")
    tran0.writeAction("slorii X17 X17 8 57")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 904")
    tran0.writeAction("slorii X18 X18 12 433")
    tran0.writeAction("slorii X18 X18 8 249")
    tran0.writeAction("slorii X18 X18 12 4049")
    tran0.writeAction("slorii X18 X18 12 2986")
    tran0.writeAction("slorii X18 X18 8 67")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
