from EFA_v2 import *
def vfill_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13504, 6572, 32617, 55404, '99.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3462")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2038")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 410")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 844")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vfill.b16 X18 99.75 ")
    tran0.writeAction("yieldt")
    return efa
