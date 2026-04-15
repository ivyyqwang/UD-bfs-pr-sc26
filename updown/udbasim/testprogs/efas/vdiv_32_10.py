from EFA_v2 import *
def vdiv_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2024631267, 2838166325, 4012489137, 433117490, 3029038956, 4223038749, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2706")
    tran0.writeAction("slorii X19 X19 12 2811")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("slorii X19 X19 12 1930")
    tran0.writeAction("slorii X19 X19 12 3435")
    tran0.writeAction("slorii X19 X19 8 227")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 413")
    tran0.writeAction("slorii X17 X17 12 217")
    tran0.writeAction("slorii X17 X17 8 50")
    tran0.writeAction("slorii X17 X17 12 3826")
    tran0.writeAction("slorii X17 X17 12 2489")
    tran0.writeAction("slorii X17 X17 8 177")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4027")
    tran0.writeAction("slorii X18 X18 12 1653")
    tran0.writeAction("slorii X18 X18 8 29")
    tran0.writeAction("slorii X18 X18 12 2888")
    tran0.writeAction("slorii X18 X18 12 2935")
    tran0.writeAction("slorii X18 X18 8 108")
    tran0.writeAction("vdiv.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
