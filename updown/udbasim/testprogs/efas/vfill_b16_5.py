from EFA_v2 import *
def vfill_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17466, 46228, 53695, 12134, '83.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 758")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 3355")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 2889")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 1091")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vfill.b16 X18 83.5 ")
    tran0.writeAction("yieldt")
    return efa
