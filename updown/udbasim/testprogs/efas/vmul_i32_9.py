from EFA_v2 import *
def vmul_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-665897230, 865174100, -1665160343, -1289852682, 424366633, 154193733, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 825")
    tran0.writeAction("slorii X19 X19 12 386")
    tran0.writeAction("slorii X19 X19 8 84")
    tran0.writeAction("slorii X19 X19 12 3460")
    tran0.writeAction("slorii X19 X19 12 3894")
    tran0.writeAction("slorii X19 X19 8 242")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2865")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("slorii X17 X17 8 246")
    tran0.writeAction("slorii X17 X17 12 2507")
    tran0.writeAction("slorii X17 X17 12 4011")
    tran0.writeAction("slorii X17 X17 8 105")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 147")
    tran0.writeAction("slorii X18 X18 12 207")
    tran0.writeAction("slorii X18 X18 8 69")
    tran0.writeAction("slorii X18 X18 12 404")
    tran0.writeAction("slorii X18 X18 12 2898")
    tran0.writeAction("slorii X18 X18 8 41")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
