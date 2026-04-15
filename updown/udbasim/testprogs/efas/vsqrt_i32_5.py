from EFA_v2 import *
def vsqrt_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [980074191, 337480245, -2104233113, -1901534137, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 321")
    tran0.writeAction("slorii X19 X19 12 3466")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("slorii X19 X19 12 934")
    tran0.writeAction("slorii X19 X19 12 2750")
    tran0.writeAction("slorii X19 X19 8 207")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2282")
    tran0.writeAction("slorii X18 X18 12 2276")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("slorii X18 X18 12 2089")
    tran0.writeAction("slorii X18 X18 12 1011")
    tran0.writeAction("slorii X18 X18 8 103")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
