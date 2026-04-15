from EFA_v2 import *
def vadd_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10207, 29875, 35528, 1703, 36006, 22085, 38549, 29149, 20863, 10291, 50944, 55684, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 106")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 2220")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1867")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 637")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1821")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 2409")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1380")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2250")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3480")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 3184")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 643")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1303")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vadd.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
