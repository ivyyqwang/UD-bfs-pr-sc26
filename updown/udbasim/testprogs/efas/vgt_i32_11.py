from EFA_v2 import *
def vgt_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [238352570, -1519067045, 2125832628, -1435664038, 360399586, -2122234310, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2647")
    tran0.writeAction("slorii X19 X19 12 1248")
    tran0.writeAction("slorii X19 X19 8 91")
    tran0.writeAction("slorii X19 X19 12 227")
    tran0.writeAction("slorii X19 X19 12 1272")
    tran0.writeAction("slorii X19 X19 8 186")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2726")
    tran0.writeAction("slorii X17 X17 12 3457")
    tran0.writeAction("slorii X17 X17 8 90")
    tran0.writeAction("slorii X17 X17 12 2027")
    tran0.writeAction("slorii X17 X17 12 1441")
    tran0.writeAction("slorii X17 X17 8 180")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2072")
    tran0.writeAction("slorii X18 X18 12 326")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("slorii X18 X18 12 343")
    tran0.writeAction("slorii X18 X18 12 2882")
    tran0.writeAction("slorii X18 X18 8 226")
    tran0.writeAction("vgt.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
