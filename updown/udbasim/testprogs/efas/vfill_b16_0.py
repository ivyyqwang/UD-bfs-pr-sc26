from EFA_v2 import *
def vfill_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [64244, 11608, 49127, 43586, '4.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2724")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3070")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 725")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 4015")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("vfill.b16 X18 4.75 ")
    tran0.writeAction("yieldt")
    return efa
