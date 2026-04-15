from EFA_v2 import *
def divi_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4807502474102203604, 19921]
    tran0.writeAction("movir X16 17079")
    tran0.writeAction("slorii X16 X16 12 2784")
    tran0.writeAction("slorii X16 X16 12 1897")
    tran0.writeAction("slorii X16 X16 12 2758")
    tran0.writeAction("slorii X16 X16 12 1236")
    tran0.writeAction("divi X16 X17 19921")
    tran0.writeAction("yieldt")
    return efa
