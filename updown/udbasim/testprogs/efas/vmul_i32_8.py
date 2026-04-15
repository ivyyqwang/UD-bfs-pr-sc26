from EFA_v2 import *
def vmul_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1146982650, -507933236, -1245529803, 1216288145, 1636690758, -1663660480, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3611")
    tran0.writeAction("slorii X19 X19 12 2445")
    tran0.writeAction("slorii X19 X19 8 204")
    tran0.writeAction("slorii X19 X19 12 1093")
    tran0.writeAction("slorii X19 X19 12 3472")
    tran0.writeAction("slorii X19 X19 8 250")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1159")
    tran0.writeAction("slorii X17 X17 12 3861")
    tran0.writeAction("slorii X17 X17 8 145")
    tran0.writeAction("slorii X17 X17 12 2908")
    tran0.writeAction("slorii X17 X17 12 697")
    tran0.writeAction("slorii X17 X17 8 53")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2509")
    tran0.writeAction("slorii X18 X18 12 1678")
    tran0.writeAction("slorii X18 X18 8 64")
    tran0.writeAction("slorii X18 X18 12 1560")
    tran0.writeAction("slorii X18 X18 12 3563")
    tran0.writeAction("slorii X18 X18 8 70")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
