from EFA_v2 import *
def vdiv_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1564041692, 711856654, -917952473, 1189939846, -1159387687, 21463538, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 678")
    tran0.writeAction("slorii X19 X19 12 3602")
    tran0.writeAction("slorii X19 X19 8 14")
    tran0.writeAction("slorii X19 X19 12 1491")
    tran0.writeAction("slorii X19 X19 12 2401")
    tran0.writeAction("slorii X19 X19 8 220")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1134")
    tran0.writeAction("slorii X17 X17 12 3338")
    tran0.writeAction("slorii X17 X17 8 134")
    tran0.writeAction("slorii X17 X17 12 3220")
    tran0.writeAction("slorii X17 X17 12 2344")
    tran0.writeAction("slorii X17 X17 8 39")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 20")
    tran0.writeAction("slorii X18 X18 12 1921")
    tran0.writeAction("slorii X18 X18 8 242")
    tran0.writeAction("slorii X18 X18 12 2990")
    tran0.writeAction("slorii X18 X18 12 1317")
    tran0.writeAction("slorii X18 X18 8 217")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
