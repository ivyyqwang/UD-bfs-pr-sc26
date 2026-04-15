from EFA_v2 import *
def vfill_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [49872, 28321, 18572, 60355, '70.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3772")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1160")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1770")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3117")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vfill.b16 X18 70.5 ")
    tran0.writeAction("yieldt")
    return efa
