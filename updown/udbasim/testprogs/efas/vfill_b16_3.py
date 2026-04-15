from EFA_v2 import *
def vfill_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [27720, 47729, 35828, 63018, '81.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3938")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2239")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 2983")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 1732")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vfill.b16 X18 81.5 ")
    tran0.writeAction("yieldt")
    return efa
