from EFA_v2 import *
def srandi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -23288")
    tran0.writeAction("slorii X16 X16 12 1261")
    tran0.writeAction("slorii X16 X16 12 2100")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("slorii X16 X16 12 109")
    tran0.writeAction("movir X17 339")
    tran0.writeAction("slorii X17 X17 12 968")
    tran0.writeAction("slorii X17 X17 12 3033")
    tran0.writeAction("slorii X17 X17 12 2438")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("srandi X16 X17 31")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
