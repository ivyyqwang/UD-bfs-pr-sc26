from EFA_v2 import *
def vfill_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [870246973, 1450586902, 681]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1383")
    tran0.writeAction("slorii X18 X18 12 1587")
    tran0.writeAction("slorii X18 X18 8 22")
    tran0.writeAction("slorii X18 X18 12 829")
    tran0.writeAction("slorii X18 X18 12 3818")
    tran0.writeAction("slorii X18 X18 8 61")
    tran0.writeAction("vfill.i32 X18 681 ")
    tran0.writeAction("yieldt")
    return efa
