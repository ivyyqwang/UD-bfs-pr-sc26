from EFA_v2 import *
def vfill_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [941, 41634, 20898, 38764, '38.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2422")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1306")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2602")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 58")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vfill.b16 X18 38.5 ")
    tran0.writeAction("yieldt")
    return efa
