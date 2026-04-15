from EFA_v2 import *
def ori_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 3117")
    tran0.writeAction("slorii X16 X16 12 831")
    tran0.writeAction("slorii X16 X16 12 857")
    tran0.writeAction("slorii X16 X16 12 2162")
    tran0.writeAction("slorii X16 X16 12 3006")
    tran0.writeAction("movir X17 -1601")
    tran0.writeAction("slorii X17 X17 12 2330")
    tran0.writeAction("slorii X17 X17 12 383")
    tran0.writeAction("slorii X17 X17 12 2002")
    tran0.writeAction("slorii X17 X17 12 315")
    tran0.writeAction("ori X16 X17 284")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
