from EFA_v2 import *
def vsqrt_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [210462991, 479172038, 2973873093, 607302371, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 456")
    tran0.writeAction("slorii X19 X19 12 3989")
    tran0.writeAction("slorii X19 X19 8 198")
    tran0.writeAction("slorii X19 X19 12 200")
    tran0.writeAction("slorii X19 X19 12 2921")
    tran0.writeAction("slorii X19 X19 8 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 579")
    tran0.writeAction("slorii X18 X18 12 690")
    tran0.writeAction("slorii X18 X18 8 227")
    tran0.writeAction("slorii X18 X18 12 2836")
    tran0.writeAction("slorii X18 X18 12 435")
    tran0.writeAction("slorii X18 X18 8 197")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
