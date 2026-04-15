from EFA_v2 import *
def vgt_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1652934721, 1690303532, 410166530, 534967632, 241753246, 536281184, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1611")
    tran0.writeAction("slorii X19 X19 12 4092")
    tran0.writeAction("slorii X19 X19 8 44")
    tran0.writeAction("slorii X19 X19 12 1576")
    tran0.writeAction("slorii X19 X19 12 1480")
    tran0.writeAction("slorii X19 X19 8 65")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 510")
    tran0.writeAction("slorii X17 X17 12 757")
    tran0.writeAction("slorii X17 X17 8 80")
    tran0.writeAction("slorii X17 X17 12 391")
    tran0.writeAction("slorii X17 X17 12 677")
    tran0.writeAction("slorii X17 X17 8 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 511")
    tran0.writeAction("slorii X18 X18 12 1792")
    tran0.writeAction("slorii X18 X18 8 96")
    tran0.writeAction("slorii X18 X18 12 230")
    tran0.writeAction("slorii X18 X18 12 2268")
    tran0.writeAction("slorii X18 X18 8 158")
    tran0.writeAction("vgt.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
