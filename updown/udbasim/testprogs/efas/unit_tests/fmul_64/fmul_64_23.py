from EFA_v2 import *
def fmul_64_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4938482938706955838, 12994731741380462461]
    tran0.writeAction("movir X16 17545")
    tran0.writeAction("slorii X16 X16 12 65")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("slorii X16 X16 12 3912")
    tran0.writeAction("slorii X16 X16 12 3646")
    tran0.writeAction("movir X17 46166")
    tran0.writeAction("slorii X17 X17 12 2298")
    tran0.writeAction("slorii X17 X17 12 2932")
    tran0.writeAction("slorii X17 X17 12 1948")
    tran0.writeAction("slorii X17 X17 12 1917")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
