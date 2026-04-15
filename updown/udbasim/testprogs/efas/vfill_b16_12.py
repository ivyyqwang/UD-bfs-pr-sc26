from EFA_v2 import *
def vfill_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2779, 61708, 58987, 64626, '93.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4039")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3686")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 3856")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 173")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vfill.b16 X18 93.75 ")
    tran0.writeAction("yieldt")
    return efa
