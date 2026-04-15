from EFA_v2 import *
def vdiv_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8418, 42820, 7394, 60079, 36458, 10190, 11537, 52148, 52719, 19957, 27132, 2558, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3754")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 462")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 2676")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 526")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3259")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 721")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 636")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 2278")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 159")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 1695")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1247")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 3294")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vdiv.b16 X19 X17 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
