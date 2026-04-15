from EFA_v2 import *
def vfill_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [33643, 13796, 46597, 12383, '87.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 773")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 2912")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 862")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 2102")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vfill.b16 X18 87.5 ")
    tran0.writeAction("yieldt")
    return efa
