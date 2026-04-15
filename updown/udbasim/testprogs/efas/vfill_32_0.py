from EFA_v2 import *
def vfill_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1565702867, 2642733823, '11.125']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2520")
    tran0.writeAction("slorii X18 X18 12 1258")
    tran0.writeAction("slorii X18 X18 8 255")
    tran0.writeAction("slorii X18 X18 12 1493")
    tran0.writeAction("slorii X18 X18 12 698")
    tran0.writeAction("slorii X18 X18 8 211")
    tran0.writeAction("vfill.32 X18 11.125 ")
    tran0.writeAction("yieldt")
    return efa
