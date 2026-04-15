from EFA_v2 import *
def vfill_32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1711590823, 2303798007, '17.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2197")
    tran0.writeAction("slorii X18 X18 12 298")
    tran0.writeAction("slorii X18 X18 8 247")
    tran0.writeAction("slorii X18 X18 12 1632")
    tran0.writeAction("slorii X18 X18 12 1229")
    tran0.writeAction("slorii X18 X18 8 167")
    tran0.writeAction("vfill.32 X18 17.0 ")
    tran0.writeAction("yieldt")
    return efa
