from EFA_v2 import *
def vmadd_b16_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [20926, 12308, 60551, 45723, 22901, 56179, 52187, 46590, 7093, 44411, 48023, 42826, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2857")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3784")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 769")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1307")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2911")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 3261")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 3511")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 1431")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2676")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3001")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 2775")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 443")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("vmadd.b16 X19 X17 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
