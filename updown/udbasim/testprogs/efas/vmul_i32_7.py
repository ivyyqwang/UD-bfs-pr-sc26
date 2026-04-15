from EFA_v2 import *
def vmul_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2038373836, -168505843, -736208622, -1976635773, 985872428, -214590184, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3935")
    tran0.writeAction("slorii X19 X19 12 1230")
    tran0.writeAction("slorii X19 X19 8 13")
    tran0.writeAction("slorii X19 X19 12 2152")
    tran0.writeAction("slorii X19 X19 12 226")
    tran0.writeAction("slorii X19 X19 8 52")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2210")
    tran0.writeAction("slorii X17 X17 12 3822")
    tran0.writeAction("slorii X17 X17 8 131")
    tran0.writeAction("slorii X17 X17 12 3393")
    tran0.writeAction("slorii X17 X17 12 3673")
    tran0.writeAction("slorii X17 X17 8 18")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3891")
    tran0.writeAction("slorii X18 X18 12 1437")
    tran0.writeAction("slorii X18 X18 8 24")
    tran0.writeAction("slorii X18 X18 12 940")
    tran0.writeAction("slorii X18 X18 12 824")
    tran0.writeAction("slorii X18 X18 8 44")
    tran0.writeAction("vmul.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
