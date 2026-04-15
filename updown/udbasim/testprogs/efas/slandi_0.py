from EFA_v2 import *
def slandi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -28809")
    tran0.writeAction("slorii X16 X16 12 1424")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("slorii X16 X16 12 3230")
    tran0.writeAction("slorii X16 X16 12 3768")
    tran0.writeAction("movir X17 10394")
    tran0.writeAction("slorii X17 X17 12 2656")
    tran0.writeAction("slorii X17 X17 12 3373")
    tran0.writeAction("slorii X17 X17 12 2151")
    tran0.writeAction("slorii X17 X17 12 3412")
    tran0.writeAction("slandi X16 X17 5")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
