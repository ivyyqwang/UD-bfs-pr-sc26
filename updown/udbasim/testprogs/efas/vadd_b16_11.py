from EFA_v2 import *
def vadd_b16_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [44644, 31498, 4604, 56226, 28341, 34404, 30290, 7756, 45281, 14858, 29768, 1545, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3514")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 287")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 1968")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 2790")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 484")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 1893")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 2150")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 96")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1860")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 928")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2830")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vadd.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
