from EFA_v2 import *
def mul_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1027777980657622252, 7409464043192827141]
    tran0.writeAction("movir X16 61884")
    tran0.writeAction("slorii X16 X16 12 2453")
    tran0.writeAction("slorii X16 X16 12 3898")
    tran0.writeAction("slorii X16 X16 12 3826")
    tran0.writeAction("slorii X16 X16 12 788")
    tran0.writeAction("movir X17 26323")
    tran0.writeAction("slorii X17 X17 12 2884")
    tran0.writeAction("slorii X17 X17 12 2638")
    tran0.writeAction("slorii X17 X17 12 2203")
    tran0.writeAction("slorii X17 X17 12 3333")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
