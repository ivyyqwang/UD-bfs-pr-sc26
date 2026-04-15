from EFA_v2 import *
def mod_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7381500159974323858, -1889154278771270286]
    tran0.writeAction("movir X16 26224")
    tran0.writeAction("slorii X16 X16 12 1460")
    tran0.writeAction("slorii X16 X16 12 2400")
    tran0.writeAction("slorii X16 X16 12 3107")
    tran0.writeAction("slorii X16 X16 12 1682")
    tran0.writeAction("movir X17 58824")
    tran0.writeAction("slorii X17 X17 12 1539")
    tran0.writeAction("slorii X17 X17 12 335")
    tran0.writeAction("slorii X17 X17 12 3805")
    tran0.writeAction("slorii X17 X17 12 3442")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
