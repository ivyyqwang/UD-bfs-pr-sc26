from EFA_v2 import *
def vdiv_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1882684912, 84250778, -159574190, -1328169801, -550736783, -1572591189, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 80")
    tran0.writeAction("slorii X19 X19 12 1424")
    tran0.writeAction("slorii X19 X19 8 154")
    tran0.writeAction("slorii X19 X19 12 2300")
    tran0.writeAction("slorii X19 X19 12 2178")
    tran0.writeAction("slorii X19 X19 8 16")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2829")
    tran0.writeAction("slorii X17 X17 12 1468")
    tran0.writeAction("slorii X17 X17 8 183")
    tran0.writeAction("slorii X17 X17 12 3943")
    tran0.writeAction("slorii X17 X17 12 3351")
    tran0.writeAction("slorii X17 X17 8 82")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2596")
    tran0.writeAction("slorii X18 X18 12 1065")
    tran0.writeAction("slorii X18 X18 8 171")
    tran0.writeAction("slorii X18 X18 12 3570")
    tran0.writeAction("slorii X18 X18 12 3180")
    tran0.writeAction("slorii X18 X18 8 113")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
