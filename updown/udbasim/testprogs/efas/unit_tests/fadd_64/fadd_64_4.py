from EFA_v2 import *
def fadd_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18323982127063773314, 17851325884856936148]
    tran0.writeAction("movir X16 65099")
    tran0.writeAction("slorii X16 X16 12 3530")
    tran0.writeAction("slorii X16 X16 12 2290")
    tran0.writeAction("slorii X16 X16 12 995")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("movir X17 63420")
    tran0.writeAction("slorii X17 X17 12 2660")
    tran0.writeAction("slorii X17 X17 12 4056")
    tran0.writeAction("slorii X17 X17 12 2594")
    tran0.writeAction("slorii X17 X17 12 1748")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
