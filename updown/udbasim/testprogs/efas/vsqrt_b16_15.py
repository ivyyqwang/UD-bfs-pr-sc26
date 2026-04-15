from EFA_v2 import *
def vsqrt_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [44350, 17693, 57754, 43639, 41181, 37915, 58142, 42639, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2727")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 3609")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 1105")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2771")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2664")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 3633")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 2369")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2573")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vsqrt.b16 X19 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
