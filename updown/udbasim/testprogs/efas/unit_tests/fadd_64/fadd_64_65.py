from EFA_v2 import *
def fadd_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1164234968474939312, 14159618893648122510]
    tran0.writeAction("movir X16 4136")
    tran0.writeAction("slorii X16 X16 12 792")
    tran0.writeAction("slorii X16 X16 12 2323")
    tran0.writeAction("slorii X16 X16 12 150")
    tran0.writeAction("slorii X16 X16 12 4016")
    tran0.writeAction("movir X17 50305")
    tran0.writeAction("slorii X17 X17 12 293")
    tran0.writeAction("slorii X17 X17 12 3302")
    tran0.writeAction("slorii X17 X17 12 3301")
    tran0.writeAction("slorii X17 X17 12 654")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
