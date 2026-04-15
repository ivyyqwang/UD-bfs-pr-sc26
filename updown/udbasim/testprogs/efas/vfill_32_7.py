from EFA_v2 import *
def vfill_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [369353339, 2762823462, '18.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2634")
    tran0.writeAction("slorii X18 X18 12 3415")
    tran0.writeAction("slorii X18 X18 8 38")
    tran0.writeAction("slorii X18 X18 12 352")
    tran0.writeAction("slorii X18 X18 12 994")
    tran0.writeAction("slorii X18 X18 8 123")
    tran0.writeAction("vfill.32 X18 18.25 ")
    tran0.writeAction("yieldt")
    return efa
