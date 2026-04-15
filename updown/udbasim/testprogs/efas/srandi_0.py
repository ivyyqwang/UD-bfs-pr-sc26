from EFA_v2 import *
def srandi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -25573")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("slorii X16 X16 12 1338")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("slorii X16 X16 12 3871")
    tran0.writeAction("movir X17 15954")
    tran0.writeAction("slorii X17 X17 12 771")
    tran0.writeAction("slorii X17 X17 12 3143")
    tran0.writeAction("slorii X17 X17 12 1761")
    tran0.writeAction("slorii X17 X17 12 1273")
    tran0.writeAction("srandi X16 X17 61")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
