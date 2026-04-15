from EFA_v2 import *
def fmul_64_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14362316873043996410, 15305630268122756996]
    tran0.writeAction("movir X16 51025")
    tran0.writeAction("slorii X16 X16 12 817")
    tran0.writeAction("slorii X16 X16 12 2537")
    tran0.writeAction("slorii X16 X16 12 1582")
    tran0.writeAction("slorii X16 X16 12 3834")
    tran0.writeAction("movir X17 54376")
    tran0.writeAction("slorii X17 X17 12 2138")
    tran0.writeAction("slorii X17 X17 12 730")
    tran0.writeAction("slorii X17 X17 12 3783")
    tran0.writeAction("slorii X17 X17 12 1924")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
