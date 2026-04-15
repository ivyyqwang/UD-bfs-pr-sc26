from EFA_v2 import *
def srorii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -7975")
    tran0.writeAction("slorii X16 X16 12 996")
    tran0.writeAction("slorii X16 X16 12 691")
    tran0.writeAction("slorii X16 X16 12 2084")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("movir X17 10649")
    tran0.writeAction("slorii X17 X17 12 2859")
    tran0.writeAction("slorii X17 X17 12 628")
    tran0.writeAction("slorii X17 X17 12 1715")
    tran0.writeAction("slorii X17 X17 12 3972")
    tran0.writeAction("srorii X16 X17 9 1663")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
