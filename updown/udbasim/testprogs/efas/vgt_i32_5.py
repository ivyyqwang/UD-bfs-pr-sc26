from EFA_v2 import *
def vgt_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1333386399, -1750612643, 1928391854, -403212389, 191732669, 1687176847, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2426")
    tran0.writeAction("slorii X19 X19 12 1989")
    tran0.writeAction("slorii X19 X19 8 93")
    tran0.writeAction("slorii X19 X19 12 2824")
    tran0.writeAction("slorii X19 X19 12 1571")
    tran0.writeAction("slorii X19 X19 8 97")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3711")
    tran0.writeAction("slorii X17 X17 12 1911")
    tran0.writeAction("slorii X17 X17 8 155")
    tran0.writeAction("slorii X17 X17 12 1839")
    tran0.writeAction("slorii X17 X17 12 236")
    tran0.writeAction("slorii X17 X17 8 174")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1609")
    tran0.writeAction("slorii X18 X18 12 70")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("slorii X18 X18 12 182")
    tran0.writeAction("slorii X18 X18 12 3483")
    tran0.writeAction("slorii X18 X18 8 189")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
