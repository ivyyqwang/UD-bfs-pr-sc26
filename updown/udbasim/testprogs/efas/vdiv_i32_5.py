from EFA_v2 import *
def vdiv_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1187844047, -1598937945, -1474505614, -653778960, -1903902258, -1593236030, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2571")
    tran0.writeAction("slorii X19 X19 12 548")
    tran0.writeAction("slorii X19 X19 8 167")
    tran0.writeAction("slorii X19 X19 12 2963")
    tran0.writeAction("slorii X19 X19 12 752")
    tran0.writeAction("slorii X19 X19 8 49")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3472")
    tran0.writeAction("slorii X17 X17 12 2079")
    tran0.writeAction("slorii X17 X17 8 240")
    tran0.writeAction("slorii X17 X17 12 2689")
    tran0.writeAction("slorii X17 X17 12 3284")
    tran0.writeAction("slorii X17 X17 8 114")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2576")
    tran0.writeAction("slorii X18 X18 12 2341")
    tran0.writeAction("slorii X18 X18 8 194")
    tran0.writeAction("slorii X18 X18 12 2280")
    tran0.writeAction("slorii X18 X18 12 1217")
    tran0.writeAction("slorii X18 X18 8 206")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
