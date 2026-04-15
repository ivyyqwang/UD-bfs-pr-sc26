from EFA_v2 import *
def vdiv_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [46822, 20567, 55617, 30159, 62165, 16863, 18818, 4745, 28705, 2659, 57614, 20992, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1884")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 3476")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 1285")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 2926")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 296")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 1053")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 3885")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1312")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3600")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 166")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1794")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vdiv.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
