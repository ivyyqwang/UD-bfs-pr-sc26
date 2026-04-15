from EFA_v2 import *
def vmul_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3752291474, 2931149064, 3966598887, 1970781502, 1794991513, 2879333977, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2795")
    tran0.writeAction("slorii X19 X19 12 1481")
    tran0.writeAction("slorii X19 X19 8 8")
    tran0.writeAction("slorii X19 X19 12 3578")
    tran0.writeAction("slorii X19 X19 12 1900")
    tran0.writeAction("slorii X19 X19 8 146")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1879")
    tran0.writeAction("slorii X17 X17 12 1981")
    tran0.writeAction("slorii X17 X17 8 62")
    tran0.writeAction("slorii X17 X17 12 3782")
    tran0.writeAction("slorii X17 X17 12 3454")
    tran0.writeAction("slorii X17 X17 8 231")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2745")
    tran0.writeAction("slorii X18 X18 12 3878")
    tran0.writeAction("slorii X18 X18 8 89")
    tran0.writeAction("slorii X18 X18 12 1711")
    tran0.writeAction("slorii X18 X18 12 3429")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
