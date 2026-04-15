from EFA_v2 import *
def vmadd_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-897208398, -1449530936, 653372728, 1407292118, -716013400, 1181503187, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2713")
    tran0.writeAction("slorii X19 X19 12 2537")
    tran0.writeAction("slorii X19 X19 8 200")
    tran0.writeAction("slorii X19 X19 12 3240")
    tran0.writeAction("slorii X19 X19 12 1455")
    tran0.writeAction("slorii X19 X19 8 178")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1342")
    tran0.writeAction("slorii X17 X17 12 402")
    tran0.writeAction("slorii X17 X17 8 214")
    tran0.writeAction("slorii X17 X17 12 623")
    tran0.writeAction("slorii X17 X17 12 429")
    tran0.writeAction("slorii X17 X17 8 56")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1126")
    tran0.writeAction("slorii X18 X18 12 3150")
    tran0.writeAction("slorii X18 X18 8 211")
    tran0.writeAction("slorii X18 X18 12 3413")
    tran0.writeAction("slorii X18 X18 12 640")
    tran0.writeAction("slorii X18 X18 8 168")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
