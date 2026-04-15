from EFA_v2 import *
def vfill_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [312395253, -1844726483, -517]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2336")
    tran0.writeAction("slorii X18 X18 12 2997")
    tran0.writeAction("slorii X18 X18 8 45")
    tran0.writeAction("slorii X18 X18 12 297")
    tran0.writeAction("slorii X18 X18 12 3781")
    tran0.writeAction("slorii X18 X18 8 245")
    tran0.writeAction("vfill.i32 X18 -517 ")
    tran0.writeAction("yieldt")
    return efa
