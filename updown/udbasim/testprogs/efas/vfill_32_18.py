from EFA_v2 import *
def vfill_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4247469575, 1566395620, '7.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1493")
    tran0.writeAction("slorii X18 X18 12 3404")
    tran0.writeAction("slorii X18 X18 8 228")
    tran0.writeAction("slorii X18 X18 12 4050")
    tran0.writeAction("slorii X18 X18 12 2878")
    tran0.writeAction("slorii X18 X18 8 7")
    tran0.writeAction("vfill.32 X18 7.75 ")
    tran0.writeAction("yieldt")
    return efa
