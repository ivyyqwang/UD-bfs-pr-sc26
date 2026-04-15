from EFA_v2 import *
def div_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5329184408603018171, 446664182242722196]
    tran0.writeAction("movir X16 46602")
    tran0.writeAction("slorii X16 X16 12 3824")
    tran0.writeAction("slorii X16 X16 12 1022")
    tran0.writeAction("slorii X16 X16 12 2731")
    tran0.writeAction("slorii X16 X16 12 3141")
    tran0.writeAction("movir X17 1586")
    tran0.writeAction("slorii X17 X17 12 3563")
    tran0.writeAction("slorii X17 X17 12 1292")
    tran0.writeAction("slorii X17 X17 12 1916")
    tran0.writeAction("slorii X17 X17 12 404")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
