from EFA_v2 import *
def vmadd_b16_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5145, 36176, 39812, 36665, 46697, 38500, 237, 64167, 43619, 40907, 51096, 31047, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2291")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2488")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 2261")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 321")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4010")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 14")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 2406")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 2918")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1940")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 3193")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2556")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2726")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vmadd.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
