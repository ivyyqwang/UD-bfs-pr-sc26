from EFA_v2 import *
def vfill_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [49747, 60183, 6314, 2472, '87.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 154")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 394")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3761")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 3109")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vfill.b16 X18 87.75 ")
    tran0.writeAction("yieldt")
    return efa
