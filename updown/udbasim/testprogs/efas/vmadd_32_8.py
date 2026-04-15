from EFA_v2 import *
def vmadd_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4099295545, 1119852007, 2299015866, 3082959807, 1782473890, 179544543, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1067")
    tran0.writeAction("slorii X19 X19 12 3989")
    tran0.writeAction("slorii X19 X19 8 231")
    tran0.writeAction("slorii X19 X19 12 3909")
    tran0.writeAction("slorii X19 X19 12 1609")
    tran0.writeAction("slorii X19 X19 8 57")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("slorii X17 X17 12 571")
    tran0.writeAction("slorii X17 X17 8 191")
    tran0.writeAction("slorii X17 X17 12 2192")
    tran0.writeAction("slorii X17 X17 12 2098")
    tran0.writeAction("slorii X17 X17 8 186")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 171")
    tran0.writeAction("slorii X18 X18 12 929")
    tran0.writeAction("slorii X18 X18 8 223")
    tran0.writeAction("slorii X18 X18 12 1699")
    tran0.writeAction("slorii X18 X18 12 3684")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
