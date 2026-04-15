from EFA_v2 import *
def vfill_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3868558673, 750741387, '18.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 715")
    tran0.writeAction("slorii X18 X18 12 3943")
    tran0.writeAction("slorii X18 X18 8 139")
    tran0.writeAction("slorii X18 X18 12 3689")
    tran0.writeAction("slorii X18 X18 12 1413")
    tran0.writeAction("slorii X18 X18 8 81")
    tran0.writeAction("vfill.32 X18 18.75 ")
    tran0.writeAction("yieldt")
    return efa
