from EFA_v2 import *
def vfill_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3863604163, 360163172, '6.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 343")
    tran0.writeAction("slorii X18 X18 12 1959")
    tran0.writeAction("slorii X18 X18 8 100")
    tran0.writeAction("slorii X18 X18 12 3684")
    tran0.writeAction("slorii X18 X18 12 2539")
    tran0.writeAction("slorii X18 X18 8 195")
    tran0.writeAction("vfill.32 X18 6.0 ")
    tran0.writeAction("yieldt")
    return efa
