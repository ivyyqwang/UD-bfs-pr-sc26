from EFA_v2 import *
def vfill_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [52096, 44370, 35460, 15231, '20.5']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 951")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 2216")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 2773")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3256")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vfill.b16 X18 20.5 ")
    tran0.writeAction("yieldt")
    return efa
