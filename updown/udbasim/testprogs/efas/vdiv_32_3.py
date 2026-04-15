from EFA_v2 import *
def vdiv_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4277602511, 3247708022, 3560877499, 4083312408, 3813728328, 3182419913, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3097")
    tran0.writeAction("slorii X19 X19 12 1047")
    tran0.writeAction("slorii X19 X19 8 118")
    tran0.writeAction("slorii X19 X19 12 4079")
    tran0.writeAction("slorii X19 X19 12 1800")
    tran0.writeAction("slorii X19 X19 8 207")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3894")
    tran0.writeAction("slorii X17 X17 12 615")
    tran0.writeAction("slorii X17 X17 8 24")
    tran0.writeAction("slorii X17 X17 12 3395")
    tran0.writeAction("slorii X17 X17 12 3757")
    tran0.writeAction("slorii X17 X17 8 187")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3034")
    tran0.writeAction("slorii X18 X18 12 4063")
    tran0.writeAction("slorii X18 X18 8 201")
    tran0.writeAction("slorii X18 X18 12 3637")
    tran0.writeAction("slorii X18 X18 12 224")
    tran0.writeAction("slorii X18 X18 8 72")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
