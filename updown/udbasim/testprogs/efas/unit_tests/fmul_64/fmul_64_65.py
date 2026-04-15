from EFA_v2 import *
def fmul_64_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6341875365719534397, 10005790997913620256]
    tran0.writeAction("movir X16 22530")
    tran0.writeAction("slorii X16 X16 12 3552")
    tran0.writeAction("slorii X16 X16 12 2911")
    tran0.writeAction("slorii X16 X16 12 2102")
    tran0.writeAction("slorii X16 X16 12 2877")
    tran0.writeAction("movir X17 35547")
    tran0.writeAction("slorii X17 X17 12 2910")
    tran0.writeAction("slorii X17 X17 12 1615")
    tran0.writeAction("slorii X17 X17 12 1812")
    tran0.writeAction("slorii X17 X17 12 3872")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
