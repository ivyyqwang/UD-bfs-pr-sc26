from EFA_v2 import *
def mul_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2189347811289162194, 8945289394991857662]
    tran0.writeAction("movir X16 7778")
    tran0.writeAction("slorii X16 X16 12 515")
    tran0.writeAction("slorii X16 X16 12 3093")
    tran0.writeAction("slorii X16 X16 12 2742")
    tran0.writeAction("slorii X16 X16 12 466")
    tran0.writeAction("movir X17 31780")
    tran0.writeAction("slorii X17 X17 12 212")
    tran0.writeAction("slorii X17 X17 12 3969")
    tran0.writeAction("slorii X17 X17 12 2287")
    tran0.writeAction("slorii X17 X17 12 4094")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
