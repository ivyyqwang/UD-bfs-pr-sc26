from EFA_v2 import *
def vfill_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3731336443, 818786302, '7.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 780")
    tran0.writeAction("slorii X18 X18 12 3503")
    tran0.writeAction("slorii X18 X18 8 254")
    tran0.writeAction("slorii X18 X18 12 3558")
    tran0.writeAction("slorii X18 X18 12 1964")
    tran0.writeAction("slorii X18 X18 8 251")
    tran0.writeAction("vfill.32 X18 7.5 ")
    tran0.writeAction("yieldt")
    return efa
