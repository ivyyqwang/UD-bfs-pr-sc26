from EFA_v2 import *
def vsub_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2757001569, 2531556381, 3480902839, 2715483123, 3011912522, 1976620307, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2414")
    tran0.writeAction("slorii X19 X19 12 1148")
    tran0.writeAction("slorii X19 X19 8 29")
    tran0.writeAction("slorii X19 X19 12 2629")
    tran0.writeAction("slorii X19 X19 12 1153")
    tran0.writeAction("slorii X19 X19 8 97")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2589")
    tran0.writeAction("slorii X17 X17 12 2811")
    tran0.writeAction("slorii X17 X17 8 243")
    tran0.writeAction("slorii X17 X17 12 3319")
    tran0.writeAction("slorii X17 X17 12 2652")
    tran0.writeAction("slorii X17 X17 8 183")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1885")
    tran0.writeAction("slorii X18 X18 12 213")
    tran0.writeAction("slorii X18 X18 8 19")
    tran0.writeAction("slorii X18 X18 12 2872")
    tran0.writeAction("slorii X18 X18 12 1571")
    tran0.writeAction("slorii X18 X18 8 74")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
