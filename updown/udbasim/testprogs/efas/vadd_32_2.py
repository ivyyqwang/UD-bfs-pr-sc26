from EFA_v2 import *
def vadd_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4188287955, 1456755678, 231812838, 4216939540, 3635399065, 1527371960, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1389")
    tran0.writeAction("slorii X19 X19 12 1107")
    tran0.writeAction("slorii X19 X19 8 222")
    tran0.writeAction("slorii X19 X19 12 3994")
    tran0.writeAction("slorii X19 X19 12 1075")
    tran0.writeAction("slorii X19 X19 8 211")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4021")
    tran0.writeAction("slorii X17 X17 12 2404")
    tran0.writeAction("slorii X17 X17 8 20")
    tran0.writeAction("slorii X17 X17 12 221")
    tran0.writeAction("slorii X17 X17 12 302")
    tran0.writeAction("slorii X17 X17 8 230")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1456")
    tran0.writeAction("slorii X18 X18 12 2520")
    tran0.writeAction("slorii X18 X18 8 184")
    tran0.writeAction("slorii X18 X18 12 3466")
    tran0.writeAction("slorii X18 X18 12 4041")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
