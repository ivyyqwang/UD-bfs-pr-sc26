from EFA_v2 import *
def fmul_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10956289906177535164, 16620382125573876544]
    tran0.writeAction("movir X16 38924")
    tran0.writeAction("slorii X16 X16 12 2297")
    tran0.writeAction("slorii X16 X16 12 3817")
    tran0.writeAction("slorii X16 X16 12 3726")
    tran0.writeAction("slorii X16 X16 12 3260")
    tran0.writeAction("movir X17 59047")
    tran0.writeAction("slorii X17 X17 12 1879")
    tran0.writeAction("slorii X17 X17 12 3090")
    tran0.writeAction("slorii X17 X17 12 338")
    tran0.writeAction("slorii X17 X17 12 2880")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
