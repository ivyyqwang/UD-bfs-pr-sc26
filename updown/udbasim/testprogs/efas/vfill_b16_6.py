from EFA_v2 import *
def vfill_b16_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [52528, 18474, 64479, 4281, '59.25']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 267")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 4029")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 1154")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3283")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vfill.b16 X18 59.25 ")
    tran0.writeAction("yieldt")
    return efa
