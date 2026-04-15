from EFA_v2 import *
def vgt_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-669835918, -1946754791, 1604376334, -2006969482, 1628943804, 18969812, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2239")
    tran0.writeAction("slorii X19 X19 12 1761")
    tran0.writeAction("slorii X19 X19 8 25")
    tran0.writeAction("slorii X19 X19 12 3457")
    tran0.writeAction("slorii X19 X19 12 797")
    tran0.writeAction("slorii X19 X19 8 114")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2182")
    tran0.writeAction("slorii X17 X17 12 19")
    tran0.writeAction("slorii X17 X17 8 118")
    tran0.writeAction("slorii X17 X17 12 1530")
    tran0.writeAction("slorii X17 X17 12 215")
    tran0.writeAction("slorii X17 X17 8 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 18")
    tran0.writeAction("slorii X18 X18 12 372")
    tran0.writeAction("slorii X18 X18 8 212")
    tran0.writeAction("slorii X18 X18 12 1553")
    tran0.writeAction("slorii X18 X18 12 1973")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("vgt.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
