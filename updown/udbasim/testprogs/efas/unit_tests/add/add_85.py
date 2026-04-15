from EFA_v2 import *
def add_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [584698562935794196, -8395804351225988147]
    tran0.writeAction("movir X16 2077")
    tran0.writeAction("slorii X16 X16 12 1091")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 2580")
    tran0.writeAction("movir X17 35708")
    tran0.writeAction("slorii X17 X17 12 454")
    tran0.writeAction("slorii X17 X17 12 3305")
    tran0.writeAction("slorii X17 X17 12 2031")
    tran0.writeAction("slorii X17 X17 12 3021")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
