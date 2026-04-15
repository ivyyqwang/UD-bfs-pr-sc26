from EFA_v2 import *
def vadd_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [188184569, 2153519522, 2665531642, 3619272636, 1496906984, 994294204, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2053")
    tran0.writeAction("slorii X19 X19 12 3097")
    tran0.writeAction("slorii X19 X19 8 162")
    tran0.writeAction("slorii X19 X19 12 179")
    tran0.writeAction("slorii X19 X19 12 1911")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3451")
    tran0.writeAction("slorii X17 X17 12 2487")
    tran0.writeAction("slorii X17 X17 8 188")
    tran0.writeAction("slorii X17 X17 12 2542")
    tran0.writeAction("slorii X17 X17 12 200")
    tran0.writeAction("slorii X17 X17 8 250")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 948")
    tran0.writeAction("slorii X18 X18 12 953")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("slorii X18 X18 12 1427")
    tran0.writeAction("slorii X18 X18 12 2300")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("vadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
