from EFA_v2 import *
def vfill_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2785954516, 3789560874, '17.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3614")
    tran0.writeAction("slorii X18 X18 12 28")
    tran0.writeAction("slorii X18 X18 8 42")
    tran0.writeAction("slorii X18 X18 12 2656")
    tran0.writeAction("slorii X18 X18 12 3658")
    tran0.writeAction("slorii X18 X18 8 212")
    tran0.writeAction("vfill.32 X18 17.25 ")
    tran0.writeAction("yieldt")
    return efa
