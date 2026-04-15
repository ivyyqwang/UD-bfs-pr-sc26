from EFA_v2 import *
def div_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5872015976087155073, -4575311335423973423]
    tran0.writeAction("movir X16 20861")
    tran0.writeAction("slorii X16 X16 12 2422")
    tran0.writeAction("slorii X16 X16 12 2882")
    tran0.writeAction("slorii X16 X16 12 383")
    tran0.writeAction("slorii X16 X16 12 385")
    tran0.writeAction("movir X17 49281")
    tran0.writeAction("slorii X17 X17 12 937")
    tran0.writeAction("slorii X17 X17 12 1243")
    tran0.writeAction("slorii X17 X17 12 966")
    tran0.writeAction("slorii X17 X17 12 2001")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
