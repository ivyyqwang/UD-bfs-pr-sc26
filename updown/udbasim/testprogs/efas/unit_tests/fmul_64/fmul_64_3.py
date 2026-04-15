from EFA_v2 import *
def fmul_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8929170367196418124, 8928563326002887414]
    tran0.writeAction("movir X16 31722")
    tran0.writeAction("slorii X16 X16 12 3218")
    tran0.writeAction("slorii X16 X16 12 995")
    tran0.writeAction("slorii X16 X16 12 2813")
    tran0.writeAction("slorii X16 X16 12 76")
    tran0.writeAction("movir X17 31720")
    tran0.writeAction("slorii X17 X17 12 2576")
    tran0.writeAction("slorii X17 X17 12 2584")
    tran0.writeAction("slorii X17 X17 12 4023")
    tran0.writeAction("slorii X17 X17 12 2806")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
