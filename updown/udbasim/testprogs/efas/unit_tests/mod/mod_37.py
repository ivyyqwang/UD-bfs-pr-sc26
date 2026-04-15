from EFA_v2 import *
def mod_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [51339729417225661, 3136226435437112116]
    tran0.writeAction("movir X16 182")
    tran0.writeAction("slorii X16 X16 12 1619")
    tran0.writeAction("slorii X16 X16 12 1598")
    tran0.writeAction("slorii X16 X16 12 3188")
    tran0.writeAction("slorii X16 X16 12 1469")
    tran0.writeAction("movir X17 11142")
    tran0.writeAction("slorii X17 X17 12 469")
    tran0.writeAction("slorii X17 X17 12 923")
    tran0.writeAction("slorii X17 X17 12 1714")
    tran0.writeAction("slorii X17 X17 12 2868")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
