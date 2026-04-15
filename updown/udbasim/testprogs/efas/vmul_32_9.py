from EFA_v2 import *
def vmul_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [615270699, 2004478192, 647642768, 3277792590, 841797983, 3717062146, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1911")
    tran0.writeAction("slorii X19 X19 12 2536")
    tran0.writeAction("slorii X19 X19 8 240")
    tran0.writeAction("slorii X19 X19 12 586")
    tran0.writeAction("slorii X19 X19 12 3145")
    tran0.writeAction("slorii X19 X19 8 43")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3125")
    tran0.writeAction("slorii X17 X17 12 3877")
    tran0.writeAction("slorii X17 X17 8 78")
    tran0.writeAction("slorii X17 X17 12 617")
    tran0.writeAction("slorii X17 X17 12 2622")
    tran0.writeAction("slorii X17 X17 8 144")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3544")
    tran0.writeAction("slorii X18 X18 12 3550")
    tran0.writeAction("slorii X18 X18 8 2")
    tran0.writeAction("slorii X18 X18 12 802")
    tran0.writeAction("slorii X18 X18 12 3281")
    tran0.writeAction("slorii X18 X18 8 95")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
