from EFA_v2 import *
def vsqrt_b16_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [28603, 25147, 21555, 28735, 54641, 42984, 30083, 47344, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1795")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1347")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1571")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 1787")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2959")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1880")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2686")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 3415")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vsqrt.b16 X19 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
