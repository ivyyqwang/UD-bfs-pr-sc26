from EFA_v2 import *
def vadd_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1811585986, 439757906, 984018214, 3969613260, 2670723408, 31534964, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 419")
    tran0.writeAction("slorii X19 X19 12 1580")
    tran0.writeAction("slorii X19 X19 8 82")
    tran0.writeAction("slorii X19 X19 12 1727")
    tran0.writeAction("slorii X19 X19 12 2715")
    tran0.writeAction("slorii X19 X19 8 194")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3785")
    tran0.writeAction("slorii X17 X17 12 2941")
    tran0.writeAction("slorii X17 X17 8 204")
    tran0.writeAction("slorii X17 X17 12 938")
    tran0.writeAction("slorii X17 X17 12 1773")
    tran0.writeAction("slorii X17 X17 8 38")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 30")
    tran0.writeAction("slorii X18 X18 12 303")
    tran0.writeAction("slorii X18 X18 8 116")
    tran0.writeAction("slorii X18 X18 12 2547")
    tran0.writeAction("slorii X18 X18 12 1")
    tran0.writeAction("slorii X18 X18 8 80")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
