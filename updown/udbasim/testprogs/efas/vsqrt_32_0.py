from EFA_v2 import *
def vsqrt_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3307836244, 823616537, 2137627723, 2945738550, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 785")
    tran0.writeAction("slorii X19 X19 12 1892")
    tran0.writeAction("slorii X19 X19 8 25")
    tran0.writeAction("slorii X19 X19 12 3154")
    tran0.writeAction("slorii X19 X19 12 2451")
    tran0.writeAction("slorii X19 X19 8 84")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2809")
    tran0.writeAction("slorii X18 X18 12 1127")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("slorii X18 X18 12 2038")
    tran0.writeAction("slorii X18 X18 12 2460")
    tran0.writeAction("slorii X18 X18 8 75")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
