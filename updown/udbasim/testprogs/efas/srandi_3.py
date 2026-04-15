from EFA_v2 import *
def srandi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 2629")
    tran0.writeAction("slorii X16 X16 12 2561")
    tran0.writeAction("slorii X16 X16 12 2471")
    tran0.writeAction("slorii X16 X16 12 64")
    tran0.writeAction("slorii X16 X16 12 716")
    tran0.writeAction("movir X17 -15932")
    tran0.writeAction("slorii X17 X17 12 269")
    tran0.writeAction("slorii X17 X17 12 3518")
    tran0.writeAction("slorii X17 X17 12 40")
    tran0.writeAction("slorii X17 X17 12 3650")
    tran0.writeAction("srandi X16 X17 51")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
