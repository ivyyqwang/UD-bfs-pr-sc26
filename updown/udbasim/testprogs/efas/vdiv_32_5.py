from EFA_v2 import *
def vdiv_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2023379318, 691855746, 827759372, 3306289946, 434772737, 947855374, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 659")
    tran0.writeAction("slorii X19 X19 12 3297")
    tran0.writeAction("slorii X19 X19 8 130")
    tran0.writeAction("slorii X19 X19 12 1929")
    tran0.writeAction("slorii X19 X19 12 2641")
    tran0.writeAction("slorii X19 X19 8 118")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3153")
    tran0.writeAction("slorii X17 X17 12 507")
    tran0.writeAction("slorii X17 X17 8 26")
    tran0.writeAction("slorii X17 X17 12 789")
    tran0.writeAction("slorii X17 X17 12 1691")
    tran0.writeAction("slorii X17 X17 8 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 903")
    tran0.writeAction("slorii X18 X18 12 3872")
    tran0.writeAction("slorii X18 X18 8 14")
    tran0.writeAction("slorii X18 X18 12 414")
    tran0.writeAction("slorii X18 X18 12 2587")
    tran0.writeAction("slorii X18 X18 8 1")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
