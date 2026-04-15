from EFA_v2 import *
def vsqrt_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1859765258, 2101072806, 689328672, 1276121848, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2003")
    tran0.writeAction("slorii X19 X19 12 3027")
    tran0.writeAction("slorii X19 X19 8 166")
    tran0.writeAction("slorii X19 X19 12 1773")
    tran0.writeAction("slorii X19 X19 12 2500")
    tran0.writeAction("slorii X19 X19 8 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1217")
    tran0.writeAction("slorii X18 X18 12 18")
    tran0.writeAction("slorii X18 X18 8 248")
    tran0.writeAction("slorii X18 X18 12 657")
    tran0.writeAction("slorii X18 X18 12 1618")
    tran0.writeAction("slorii X18 X18 8 32")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
