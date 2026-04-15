from EFA_v2 import *
def vdiv_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1061808315, 2670032346, 3454646347, 1372649924, 3112025528, 938351251, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2546")
    tran0.writeAction("slorii X19 X19 12 1397")
    tran0.writeAction("slorii X19 X19 8 218")
    tran0.writeAction("slorii X19 X19 12 1012")
    tran0.writeAction("slorii X19 X19 12 2536")
    tran0.writeAction("slorii X19 X19 8 187")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1309")
    tran0.writeAction("slorii X17 X17 12 249")
    tran0.writeAction("slorii X17 X17 8 196")
    tran0.writeAction("slorii X17 X17 12 3294")
    tran0.writeAction("slorii X17 X17 12 2488")
    tran0.writeAction("slorii X17 X17 8 75")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 894")
    tran0.writeAction("slorii X18 X18 12 3610")
    tran0.writeAction("slorii X18 X18 8 147")
    tran0.writeAction("slorii X18 X18 12 2967")
    tran0.writeAction("slorii X18 X18 12 3517")
    tran0.writeAction("slorii X18 X18 8 184")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
