from EFA_v2 import *
def vfill_b16_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17395, 61211, 40511, 12729, '10.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 795")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2531")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 3825")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1087")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vfill.b16 X18 10.25 ")
    tran0.writeAction("yieldt")
    return efa
