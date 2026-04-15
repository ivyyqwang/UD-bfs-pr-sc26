from EFA_v2 import *
def vsqrt_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12043, 34612, 16457, 3505, 17804, 59701, 59522, 6592, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 219")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 1028")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2163")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 752")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 412")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3720")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3731")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1112")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("vsqrt.b16 X19 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
