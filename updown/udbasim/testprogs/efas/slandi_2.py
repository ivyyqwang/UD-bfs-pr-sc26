from EFA_v2 import *
def slandi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 27147")
    tran0.writeAction("slorii X16 X16 12 102")
    tran0.writeAction("slorii X16 X16 12 3912")
    tran0.writeAction("slorii X16 X16 12 3718")
    tran0.writeAction("slorii X16 X16 12 2992")
    tran0.writeAction("movir X17 5936")
    tran0.writeAction("slorii X17 X17 12 2310")
    tran0.writeAction("slorii X17 X17 12 2436")
    tran0.writeAction("slorii X17 X17 12 1450")
    tran0.writeAction("slorii X17 X17 12 1271")
    tran0.writeAction("slandi X16 X17 29")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
