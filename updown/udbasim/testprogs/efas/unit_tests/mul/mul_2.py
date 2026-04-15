from EFA_v2 import *
def mul_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8841948985971746715, -3146976928239757684]
    tran0.writeAction("movir X16 34123")
    tran0.writeAction("slorii X16 X16 12 355")
    tran0.writeAction("slorii X16 X16 12 3697")
    tran0.writeAction("slorii X16 X16 12 117")
    tran0.writeAction("slorii X16 X16 12 2149")
    tran0.writeAction("movir X17 54355")
    tran0.writeAction("slorii X17 X17 12 2834")
    tran0.writeAction("slorii X17 X17 12 2107")
    tran0.writeAction("slorii X17 X17 12 3765")
    tran0.writeAction("slorii X17 X17 12 1676")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
