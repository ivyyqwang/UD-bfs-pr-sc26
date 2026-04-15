from EFA_v2 import *
def mod_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7696581643398050993, -7460932746483256222]
    tran0.writeAction("movir X16 38192")
    tran0.writeAction("slorii X16 X16 12 1020")
    tran0.writeAction("slorii X16 X16 12 1544")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("slorii X16 X16 12 2895")
    tran0.writeAction("movir X17 39029")
    tran0.writeAction("slorii X17 X17 12 1811")
    tran0.writeAction("slorii X17 X17 12 608")
    tran0.writeAction("slorii X17 X17 12 3219")
    tran0.writeAction("slorii X17 X17 12 1122")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
