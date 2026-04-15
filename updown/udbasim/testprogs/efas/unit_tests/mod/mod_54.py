from EFA_v2 import *
def mod_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8095530951476538679, -5805051658047494427]
    tran0.writeAction("movir X16 36774")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("slorii X16 X16 12 3545")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("slorii X16 X16 12 713")
    tran0.writeAction("movir X17 44912")
    tran0.writeAction("slorii X17 X17 12 1284")
    tran0.writeAction("slorii X17 X17 12 1539")
    tran0.writeAction("slorii X17 X17 12 1174")
    tran0.writeAction("slorii X17 X17 12 1765")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
