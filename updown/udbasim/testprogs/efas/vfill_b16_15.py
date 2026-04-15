from EFA_v2 import *
def vfill_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9901, 19180, 42953, 17565, '6.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1097")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 2684")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1198")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 618")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vfill.b16 X18 6.0 ")
    tran0.writeAction("yieldt")
    return efa
