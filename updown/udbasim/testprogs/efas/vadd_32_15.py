from EFA_v2 import *
def vadd_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2633389489, 2839944609, 513371394, 4101237371, 1763026507, 2085302721, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2708")
    tran0.writeAction("slorii X19 X19 12 1565")
    tran0.writeAction("slorii X19 X19 8 161")
    tran0.writeAction("slorii X19 X19 12 2511")
    tran0.writeAction("slorii X19 X19 12 1621")
    tran0.writeAction("slorii X19 X19 8 177")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3911")
    tran0.writeAction("slorii X17 X17 12 1002")
    tran0.writeAction("slorii X17 X17 8 123")
    tran0.writeAction("slorii X17 X17 12 489")
    tran0.writeAction("slorii X17 X17 12 2413")
    tran0.writeAction("slorii X17 X17 8 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1988")
    tran0.writeAction("slorii X18 X18 12 2865")
    tran0.writeAction("slorii X18 X18 8 193")
    tran0.writeAction("slorii X18 X18 12 1681")
    tran0.writeAction("slorii X18 X18 12 1446")
    tran0.writeAction("slorii X18 X18 8 75")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
