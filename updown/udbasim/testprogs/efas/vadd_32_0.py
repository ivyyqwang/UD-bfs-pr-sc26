from EFA_v2 import *
def vadd_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2315104202, 663844889, 28099205, 1929833239, 4284893040, 1826465012, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 633")
    tran0.writeAction("slorii X19 X19 12 376")
    tran0.writeAction("slorii X19 X19 8 25")
    tran0.writeAction("slorii X19 X19 12 2207")
    tran0.writeAction("slorii X19 X19 12 3503")
    tran0.writeAction("slorii X19 X19 8 202")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1840")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("slorii X17 X17 8 23")
    tran0.writeAction("slorii X17 X17 12 26")
    tran0.writeAction("slorii X17 X17 12 3266")
    tran0.writeAction("slorii X17 X17 8 133")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1741")
    tran0.writeAction("slorii X18 X18 12 3492")
    tran0.writeAction("slorii X18 X18 8 244")
    tran0.writeAction("slorii X18 X18 12 4086")
    tran0.writeAction("slorii X18 X18 12 1607")
    tran0.writeAction("slorii X18 X18 8 112")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
