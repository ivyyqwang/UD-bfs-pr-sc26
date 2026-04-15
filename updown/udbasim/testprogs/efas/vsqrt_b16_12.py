from EFA_v2 import *
def vsqrt_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [33610, 47123, 8990, 20952, 6285, 31969, 882, 50890, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1309")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 561")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2945")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 2100")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3180")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 55")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 1998")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 392")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vsqrt.b16 X19 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
