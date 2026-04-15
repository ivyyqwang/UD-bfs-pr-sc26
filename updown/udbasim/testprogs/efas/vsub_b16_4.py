from EFA_v2 import *
def vsub_b16_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14123, 63291, 43746, 36084, 29806, 29139, 40564, 6434, 18639, 59358, 51866, 20179, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2255")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 2734")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3955")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 882")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 402")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 2535")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 1821")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 1862")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1261")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 3241")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3709")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 1164")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vsub.b16 X19 X17 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
