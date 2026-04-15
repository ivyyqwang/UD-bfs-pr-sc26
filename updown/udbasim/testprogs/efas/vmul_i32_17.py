from EFA_v2 import *
def vmul_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-121081886, 2083806948, 1126598211, 303251722, -1317943580, 1644149987, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1987")
    tran0.writeAction("slorii X19 X19 12 1118")
    tran0.writeAction("slorii X19 X19 8 228")
    tran0.writeAction("slorii X19 X19 12 3980")
    tran0.writeAction("slorii X19 X19 12 2159")
    tran0.writeAction("slorii X19 X19 8 226")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 289")
    tran0.writeAction("slorii X17 X17 12 833")
    tran0.writeAction("slorii X17 X17 8 10")
    tran0.writeAction("slorii X17 X17 12 1074")
    tran0.writeAction("slorii X17 X17 12 1670")
    tran0.writeAction("slorii X17 X17 8 67")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1567")
    tran0.writeAction("slorii X18 X18 12 4028")
    tran0.writeAction("slorii X18 X18 8 227")
    tran0.writeAction("slorii X18 X18 12 2839")
    tran0.writeAction("slorii X18 X18 12 454")
    tran0.writeAction("slorii X18 X18 8 228")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
