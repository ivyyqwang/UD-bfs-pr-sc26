from EFA_v2 import *
def vfill_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [901642536, 2168010250, '11.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2067")
    tran0.writeAction("slorii X18 X18 12 2358")
    tran0.writeAction("slorii X18 X18 8 10")
    tran0.writeAction("slorii X18 X18 12 859")
    tran0.writeAction("slorii X18 X18 12 3577")
    tran0.writeAction("slorii X18 X18 8 40")
    tran0.writeAction("vfill.32 X18 11.5 ")
    tran0.writeAction("yieldt")
    return efa
