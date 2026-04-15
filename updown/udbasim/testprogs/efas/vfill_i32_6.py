from EFA_v2 import *
def vfill_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1430607954, 1772293412, -394]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1690")
    tran0.writeAction("slorii X18 X18 12 781")
    tran0.writeAction("slorii X18 X18 8 36")
    tran0.writeAction("slorii X18 X18 12 1364")
    tran0.writeAction("slorii X18 X18 12 1368")
    tran0.writeAction("slorii X18 X18 8 82")
    tran0.writeAction("vfill.i32 X18 -394 ")
    tran0.writeAction("yieldt")
    return efa
