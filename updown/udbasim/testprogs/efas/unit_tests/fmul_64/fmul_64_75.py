from EFA_v2 import *
def fmul_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10962594165985506581, 7239340561106523339]
    tran0.writeAction("movir X16 38946")
    tran0.writeAction("slorii X16 X16 12 3924")
    tran0.writeAction("slorii X16 X16 12 4040")
    tran0.writeAction("slorii X16 X16 12 1375")
    tran0.writeAction("slorii X16 X16 12 1301")
    tran0.writeAction("movir X17 25719")
    tran0.writeAction("slorii X17 X17 12 1246")
    tran0.writeAction("slorii X17 X17 12 632")
    tran0.writeAction("slorii X17 X17 12 3405")
    tran0.writeAction("slorii X17 X17 12 1227")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
