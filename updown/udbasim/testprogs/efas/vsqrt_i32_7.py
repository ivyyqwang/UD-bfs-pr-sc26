from EFA_v2 import *
def vsqrt_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2058704612, 285733381, -1866411268, 773897155, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 272")
    tran0.writeAction("slorii X19 X19 12 2034")
    tran0.writeAction("slorii X19 X19 8 5")
    tran0.writeAction("slorii X19 X19 12 2132")
    tran0.writeAction("slorii X19 X19 12 2729")
    tran0.writeAction("slorii X19 X19 8 28")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 738")
    tran0.writeAction("slorii X18 X18 12 187")
    tran0.writeAction("slorii X18 X18 8 195")
    tran0.writeAction("slorii X18 X18 12 2316")
    tran0.writeAction("slorii X18 X18 12 210")
    tran0.writeAction("slorii X18 X18 8 252")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
