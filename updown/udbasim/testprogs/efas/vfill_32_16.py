from EFA_v2 import *
def vfill_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1423994010, 2748368242, '8.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2621")
    tran0.writeAction("slorii X18 X18 12 197")
    tran0.writeAction("slorii X18 X18 8 114")
    tran0.writeAction("slorii X18 X18 12 1358")
    tran0.writeAction("slorii X18 X18 12 108")
    tran0.writeAction("slorii X18 X18 8 154")
    tran0.writeAction("vfill.32 X18 8.5 ")
    tran0.writeAction("yieldt")
    return efa
