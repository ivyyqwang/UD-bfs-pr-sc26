from EFA_v2 import *
def srandi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 7341")
    tran0.writeAction("slorii X16 X16 12 1949")
    tran0.writeAction("slorii X16 X16 12 3351")
    tran0.writeAction("slorii X16 X16 12 1299")
    tran0.writeAction("slorii X16 X16 12 777")
    tran0.writeAction("movir X17 8863")
    tran0.writeAction("slorii X17 X17 12 905")
    tran0.writeAction("slorii X17 X17 12 950")
    tran0.writeAction("slorii X17 X17 12 2495")
    tran0.writeAction("slorii X17 X17 12 746")
    tran0.writeAction("srandi X16 X17 25")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
