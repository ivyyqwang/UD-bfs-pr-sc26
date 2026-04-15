from EFA_v2 import *
def vfill_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4574, 25702, 24533, 36060, '3.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2253")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1533")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1606")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 285")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("vfill.b16 X18 3.75 ")
    tran0.writeAction("yieldt")
    return efa
