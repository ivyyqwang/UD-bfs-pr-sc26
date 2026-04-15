from EFA_v2 import *
def vdiv_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [283278178, 728427818, -743016024, 331066418, -951580091, 91989001, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 694")
    tran0.writeAction("slorii X19 X19 12 2797")
    tran0.writeAction("slorii X19 X19 8 42")
    tran0.writeAction("slorii X19 X19 12 270")
    tran0.writeAction("slorii X19 X19 12 635")
    tran0.writeAction("slorii X19 X19 8 98")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 315")
    tran0.writeAction("slorii X17 X17 12 2988")
    tran0.writeAction("slorii X17 X17 8 50")
    tran0.writeAction("slorii X17 X17 12 3387")
    tran0.writeAction("slorii X17 X17 12 1657")
    tran0.writeAction("slorii X17 X17 8 168")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 87")
    tran0.writeAction("slorii X18 X18 12 2980")
    tran0.writeAction("slorii X18 X18 8 9")
    tran0.writeAction("slorii X18 X18 12 3188")
    tran0.writeAction("slorii X18 X18 12 2058")
    tran0.writeAction("slorii X18 X18 8 69")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
