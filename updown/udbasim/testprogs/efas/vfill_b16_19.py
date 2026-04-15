from EFA_v2 import *
def vfill_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [22, 56009, 36990, 34605, '81.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2162")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 2311")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3500")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vfill.b16 X18 81.0 ")
    tran0.writeAction("yieldt")
    return efa
