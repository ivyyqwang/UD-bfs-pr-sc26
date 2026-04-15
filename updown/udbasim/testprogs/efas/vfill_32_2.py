from EFA_v2 import *
def vfill_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [306291336, 919946631, '1.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 877")
    tran0.writeAction("slorii X18 X18 12 1349")
    tran0.writeAction("slorii X18 X18 8 135")
    tran0.writeAction("slorii X18 X18 12 292")
    tran0.writeAction("slorii X18 X18 12 418")
    tran0.writeAction("slorii X18 X18 8 136")
    tran0.writeAction("vfill.32 X18 1.0 ")
    tran0.writeAction("yieldt")
    return efa
