from EFA_v2 import *
def vsqrt_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [746818312, -664864380, -1638652171, 2078109988, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3461")
    tran0.writeAction("slorii X19 X19 12 3833")
    tran0.writeAction("slorii X19 X19 8 132")
    tran0.writeAction("slorii X19 X19 12 712")
    tran0.writeAction("slorii X19 X19 12 907")
    tran0.writeAction("slorii X19 X19 8 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1981")
    tran0.writeAction("slorii X18 X18 12 3441")
    tran0.writeAction("slorii X18 X18 8 36")
    tran0.writeAction("slorii X18 X18 12 2533")
    tran0.writeAction("slorii X18 X18 12 1062")
    tran0.writeAction("slorii X18 X18 8 245")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
