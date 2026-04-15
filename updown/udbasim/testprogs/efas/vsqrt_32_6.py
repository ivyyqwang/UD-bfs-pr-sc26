from EFA_v2 import *
def vsqrt_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1982496778, 2602339847, 4094034450, 610941553, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2481")
    tran0.writeAction("slorii X19 X19 12 3214")
    tran0.writeAction("slorii X19 X19 8 7")
    tran0.writeAction("slorii X19 X19 12 1890")
    tran0.writeAction("slorii X19 X19 12 2688")
    tran0.writeAction("slorii X19 X19 8 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 582")
    tran0.writeAction("slorii X18 X18 12 2618")
    tran0.writeAction("slorii X18 X18 8 113")
    tran0.writeAction("slorii X18 X18 12 3904")
    tran0.writeAction("slorii X18 X18 12 1538")
    tran0.writeAction("slorii X18 X18 8 18")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
