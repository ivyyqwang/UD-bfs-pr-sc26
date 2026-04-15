from EFA_v2 import *
def vsqrt_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1105220809, 1248411234, 716011732, 1856863375, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1190")
    tran0.writeAction("slorii X19 X19 12 2366")
    tran0.writeAction("slorii X19 X19 8 98")
    tran0.writeAction("slorii X19 X19 12 1054")
    tran0.writeAction("slorii X19 X19 12 84")
    tran0.writeAction("slorii X19 X19 8 201")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1770")
    tran0.writeAction("slorii X18 X18 12 3452")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("slorii X18 X18 12 682")
    tran0.writeAction("slorii X18 X18 12 3448")
    tran0.writeAction("slorii X18 X18 8 212")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
