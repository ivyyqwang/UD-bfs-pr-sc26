from EFA_v2 import *
def fsqrt_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16377448131882472668]
    tran0.writeAction("movir X16 58184")
    tran0.writeAction("slorii X16 X16 12 1572")
    tran0.writeAction("slorii X16 X16 12 3572")
    tran0.writeAction("slorii X16 X16 12 981")
    tran0.writeAction("slorii X16 X16 12 1244")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
