from EFA_v2 import *
def vfill_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1013273745, 70568928, '5.125']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 67")
    tran0.writeAction("slorii X18 X18 12 1227")
    tran0.writeAction("slorii X18 X18 8 224")
    tran0.writeAction("slorii X18 X18 12 966")
    tran0.writeAction("slorii X18 X18 12 1364")
    tran0.writeAction("slorii X18 X18 8 145")
    tran0.writeAction("vfill.32 X18 5.125 ")
    tran0.writeAction("yieldt")
    return efa
