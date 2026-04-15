from EFA_v2 import *
def mod_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [996254293620793938, 4913683502047788145]
    tran0.writeAction("movir X16 3539")
    tran0.writeAction("slorii X16 X16 12 1664")
    tran0.writeAction("slorii X16 X16 12 109")
    tran0.writeAction("slorii X16 X16 12 922")
    tran0.writeAction("slorii X16 X16 12 594")
    tran0.writeAction("movir X17 17456")
    tran0.writeAction("slorii X17 X17 12 3729")
    tran0.writeAction("slorii X17 X17 12 3198")
    tran0.writeAction("slorii X17 X17 12 1047")
    tran0.writeAction("slorii X17 X17 12 3185")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
