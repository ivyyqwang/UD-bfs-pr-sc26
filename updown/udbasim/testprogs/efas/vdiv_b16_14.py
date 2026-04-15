from EFA_v2 import *
def vdiv_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [52686, 13882, 52107, 35203, 41783, 30721, 48370, 46631, 50955, 64715, 20847, 37437, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2200")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3256")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 867")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 3292")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2914")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3023")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 1920")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 2611")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2339")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 1302")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 4044")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 3184")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vdiv.b16 X19 X17 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
