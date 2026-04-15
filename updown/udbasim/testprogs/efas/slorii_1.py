from EFA_v2 import *
def slorii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 9737")
    tran0.writeAction("slorii X16 X16 12 1167")
    tran0.writeAction("slorii X16 X16 12 3661")
    tran0.writeAction("slorii X16 X16 12 3027")
    tran0.writeAction("slorii X16 X16 12 2331")
    tran0.writeAction("movir X17 -16416")
    tran0.writeAction("slorii X17 X17 12 2861")
    tran0.writeAction("slorii X17 X17 12 1579")
    tran0.writeAction("slorii X17 X17 12 615")
    tran0.writeAction("slorii X17 X17 12 479")
    tran0.writeAction("slorii X16 X17 5 1952")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
