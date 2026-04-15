from EFA_v2 import *
def vmul_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [507513895, 2104777342, -1697900151, -1528597615, -1769202836, 2107976846, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2007")
    tran0.writeAction("slorii X19 X19 12 1114")
    tran0.writeAction("slorii X19 X19 8 126")
    tran0.writeAction("slorii X19 X19 12 484")
    tran0.writeAction("slorii X19 X19 12 12")
    tran0.writeAction("slorii X19 X19 8 39")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2638")
    tran0.writeAction("slorii X17 X17 12 883")
    tran0.writeAction("slorii X17 X17 8 145")
    tran0.writeAction("slorii X17 X17 12 2476")
    tran0.writeAction("slorii X17 X17 12 3097")
    tran0.writeAction("slorii X17 X17 8 137")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2010")
    tran0.writeAction("slorii X18 X18 12 1324")
    tran0.writeAction("slorii X18 X18 8 142")
    tran0.writeAction("slorii X18 X18 12 2408")
    tran0.writeAction("slorii X18 X18 12 3099")
    tran0.writeAction("slorii X18 X18 8 108")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
