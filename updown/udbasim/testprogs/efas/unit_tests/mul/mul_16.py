from EFA_v2 import *
def mul_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1888978558494776876, 4024607519579004221]
    tran0.writeAction("movir X16 6710")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 3487")
    tran0.writeAction("slorii X16 X16 12 1681")
    tran0.writeAction("slorii X16 X16 12 3628")
    tran0.writeAction("movir X17 14298")
    tran0.writeAction("slorii X17 X17 12 1139")
    tran0.writeAction("slorii X17 X17 12 1852")
    tran0.writeAction("slorii X17 X17 12 3573")
    tran0.writeAction("slorii X17 X17 12 3389")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
