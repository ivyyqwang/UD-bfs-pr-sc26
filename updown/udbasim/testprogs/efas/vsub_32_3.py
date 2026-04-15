from EFA_v2 import *
def vsub_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1284704505, 1868369365, 936774450, 612607650, 394113151, 3650459624, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1781")
    tran0.writeAction("slorii X19 X19 12 3341")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("slorii X19 X19 12 1225")
    tran0.writeAction("slorii X19 X19 12 776")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 584")
    tran0.writeAction("slorii X17 X17 12 934")
    tran0.writeAction("slorii X17 X17 8 162")
    tran0.writeAction("slorii X17 X17 12 893")
    tran0.writeAction("slorii X17 X17 12 1547")
    tran0.writeAction("slorii X17 X17 8 50")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3481")
    tran0.writeAction("slorii X18 X18 12 1431")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("slorii X18 X18 12 375")
    tran0.writeAction("slorii X18 X18 12 3504")
    tran0.writeAction("slorii X18 X18 8 127")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
