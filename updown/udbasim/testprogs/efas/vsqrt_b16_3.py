from EFA_v2 import *
def vsqrt_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [25578, 61994, 31022, 60137, 49984, 46681, 6886, 36408, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3758")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1938")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3874")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 1598")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2275")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 430")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2917")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3124")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vsqrt.b16 X19 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
