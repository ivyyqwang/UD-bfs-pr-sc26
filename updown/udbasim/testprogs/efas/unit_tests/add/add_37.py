from EFA_v2 import *
def add_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-428873488772872522, -62297065542644159]
    tran0.writeAction("movir X16 64012")
    tran0.writeAction("slorii X16 X16 12 1373")
    tran0.writeAction("slorii X16 X16 12 1424")
    tran0.writeAction("slorii X16 X16 12 452")
    tran0.writeAction("slorii X16 X16 12 1718")
    tran0.writeAction("movir X17 65314")
    tran0.writeAction("slorii X17 X17 12 2770")
    tran0.writeAction("slorii X17 X17 12 1569")
    tran0.writeAction("slorii X17 X17 12 3200")
    tran0.writeAction("slorii X17 X17 12 3649")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
