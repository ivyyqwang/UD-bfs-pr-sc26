from EFA_v2 import *
def vsqrt_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [19422, 15209, 48975, 63995, 19881, 45911, 58434, 43762, 4]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3999")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3060")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 950")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1213")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2735")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3652")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2869")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1242")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vsqrt.b16 X19 X18 4 ")
    tran0.writeAction("yieldt")
    return efa
