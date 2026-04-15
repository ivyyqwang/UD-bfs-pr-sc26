from EFA_v2 import *
def vgt_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3931236792, 696723506, 2129361851, 2150461575, 2256382658, 1869268351, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 664")
    tran0.writeAction("slorii X19 X19 12 1832")
    tran0.writeAction("slorii X19 X19 8 50")
    tran0.writeAction("slorii X19 X19 12 3749")
    tran0.writeAction("slorii X19 X19 12 489")
    tran0.writeAction("slorii X19 X19 8 184")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2050")
    tran0.writeAction("slorii X17 X17 12 3440")
    tran0.writeAction("slorii X17 X17 8 135")
    tran0.writeAction("slorii X17 X17 12 2030")
    tran0.writeAction("slorii X17 X17 12 2939")
    tran0.writeAction("slorii X17 X17 8 187")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1782")
    tran0.writeAction("slorii X18 X18 12 2757")
    tran0.writeAction("slorii X18 X18 8 127")
    tran0.writeAction("slorii X18 X18 12 2151")
    tran0.writeAction("slorii X18 X18 12 3498")
    tran0.writeAction("slorii X18 X18 8 194")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
