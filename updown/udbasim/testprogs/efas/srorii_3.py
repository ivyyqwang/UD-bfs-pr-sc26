from EFA_v2 import *
def srorii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 31395")
    tran0.writeAction("slorii X16 X16 12 1250")
    tran0.writeAction("slorii X16 X16 12 2016")
    tran0.writeAction("slorii X16 X16 12 3056")
    tran0.writeAction("slorii X16 X16 12 3162")
    tran0.writeAction("movir X17 -17097")
    tran0.writeAction("slorii X17 X17 12 457")
    tran0.writeAction("slorii X17 X17 12 2032")
    tran0.writeAction("slorii X17 X17 12 1780")
    tran0.writeAction("slorii X17 X17 12 2373")
    tran0.writeAction("srorii X16 X17 1 826")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
