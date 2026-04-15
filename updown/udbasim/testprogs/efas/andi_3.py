from EFA_v2 import *
def andi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -601")
    tran0.writeAction("slorii X16 X16 12 692")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("slorii X16 X16 12 62")
    tran0.writeAction("slorii X16 X16 12 1285")
    tran0.writeAction("movir X17 10721")
    tran0.writeAction("slorii X17 X17 12 2408")
    tran0.writeAction("slorii X17 X17 12 3791")
    tran0.writeAction("slorii X17 X17 12 2426")
    tran0.writeAction("slorii X17 X17 12 2563")
    tran0.writeAction("andi X16 X17 -24016")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
