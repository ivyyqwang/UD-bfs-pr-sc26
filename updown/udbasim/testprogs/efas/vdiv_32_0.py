from EFA_v2 import *
def vdiv_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [666398421, 1582447683, 2273367241, 1378550133, 2444064419, 3590145371, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1509")
    tran0.writeAction("slorii X19 X19 12 572")
    tran0.writeAction("slorii X19 X19 8 67")
    tran0.writeAction("slorii X19 X19 12 635")
    tran0.writeAction("slorii X19 X19 12 2158")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1314")
    tran0.writeAction("slorii X17 X17 12 2817")
    tran0.writeAction("slorii X17 X17 8 117")
    tran0.writeAction("slorii X17 X17 12 2168")
    tran0.writeAction("slorii X17 X17 12 212")
    tran0.writeAction("slorii X17 X17 8 201")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3423")
    tran0.writeAction("slorii X18 X18 12 3397")
    tran0.writeAction("slorii X18 X18 8 91")
    tran0.writeAction("slorii X18 X18 12 2330")
    tran0.writeAction("slorii X18 X18 12 3446")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
