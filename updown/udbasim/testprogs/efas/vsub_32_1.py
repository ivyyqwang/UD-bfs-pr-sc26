from EFA_v2 import *
def vsub_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [887224784, 4161396422, 3295402520, 3491150662, 3961298824, 1386849619, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3968")
    tran0.writeAction("slorii X19 X19 12 2526")
    tran0.writeAction("slorii X19 X19 8 198")
    tran0.writeAction("slorii X19 X19 12 846")
    tran0.writeAction("slorii X19 X19 12 505")
    tran0.writeAction("slorii X19 X19 8 208")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3329")
    tran0.writeAction("slorii X17 X17 12 1723")
    tran0.writeAction("slorii X17 X17 8 70")
    tran0.writeAction("slorii X17 X17 12 3142")
    tran0.writeAction("slorii X17 X17 12 3034")
    tran0.writeAction("slorii X17 X17 8 24")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1322")
    tran0.writeAction("slorii X18 X18 12 2469")
    tran0.writeAction("slorii X18 X18 8 83")
    tran0.writeAction("slorii X18 X18 12 3777")
    tran0.writeAction("slorii X18 X18 12 3231")
    tran0.writeAction("slorii X18 X18 8 136")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
