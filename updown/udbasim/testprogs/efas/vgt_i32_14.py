from EFA_v2 import *
def vgt_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-918770954, 3555612, 1908988756, -699700747, -604439848, 1747960479, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3")
    tran0.writeAction("slorii X19 X19 12 1601")
    tran0.writeAction("slorii X19 X19 8 28")
    tran0.writeAction("slorii X19 X19 12 3219")
    tran0.writeAction("slorii X19 X19 12 3242")
    tran0.writeAction("slorii X19 X19 8 246")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3428")
    tran0.writeAction("slorii X17 X17 12 2921")
    tran0.writeAction("slorii X17 X17 8 245")
    tran0.writeAction("slorii X17 X17 12 1820")
    tran0.writeAction("slorii X17 X17 12 2267")
    tran0.writeAction("slorii X17 X17 8 84")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1666")
    tran0.writeAction("slorii X18 X18 12 4034")
    tran0.writeAction("slorii X18 X18 8 159")
    tran0.writeAction("slorii X18 X18 12 3519")
    tran0.writeAction("slorii X18 X18 12 2298")
    tran0.writeAction("slorii X18 X18 8 216")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
