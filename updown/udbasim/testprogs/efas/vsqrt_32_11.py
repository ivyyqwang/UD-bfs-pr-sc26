from EFA_v2 import *
def vsqrt_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1887470330, 921472944, 3805502596, 1487024584, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 878")
    tran0.writeAction("slorii X19 X19 12 3215")
    tran0.writeAction("slorii X19 X19 8 176")
    tran0.writeAction("slorii X19 X19 12 1800")
    tran0.writeAction("slorii X19 X19 12 130")
    tran0.writeAction("slorii X19 X19 8 250")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1418")
    tran0.writeAction("slorii X18 X18 12 561")
    tran0.writeAction("slorii X18 X18 8 200")
    tran0.writeAction("slorii X18 X18 12 3629")
    tran0.writeAction("slorii X18 X18 12 860")
    tran0.writeAction("slorii X18 X18 8 132")
    tran0.writeAction("vsqrt.32 X19 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
