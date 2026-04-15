from EFA_v2 import *
def sar_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -8291")
    tran0.writeAction("slorii X16 X16 12 977")
    tran0.writeAction("slorii X16 X16 12 3900")
    tran0.writeAction("slorii X16 X16 12 714")
    tran0.writeAction("slorii X16 X16 12 3563")
    tran0.writeAction("movir X17 -14531")
    tran0.writeAction("slorii X17 X17 12 2594")
    tran0.writeAction("slorii X17 X17 12 1717")
    tran0.writeAction("slorii X17 X17 12 2219")
    tran0.writeAction("slorii X17 X17 12 2393")
    tran0.writeAction("movir X18 -12797")
    tran0.writeAction("slorii X18 X18 12 3916")
    tran0.writeAction("slorii X18 X18 12 4012")
    tran0.writeAction("slorii X18 X18 12 3530")
    tran0.writeAction("slorii X18 X18 12 3915")
    tran0.writeAction("sar X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
