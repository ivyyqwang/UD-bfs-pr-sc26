from EFA_v2 import *
def sar_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 16236")
    tran0.writeAction("slorii X16 X16 12 2193")
    tran0.writeAction("slorii X16 X16 12 2175")
    tran0.writeAction("slorii X16 X16 12 3460")
    tran0.writeAction("slorii X16 X16 12 3227")
    tran0.writeAction("movir X17 9355")
    tran0.writeAction("slorii X17 X17 12 1942")
    tran0.writeAction("slorii X17 X17 12 362")
    tran0.writeAction("slorii X17 X17 12 1784")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("movir X18 17909")
    tran0.writeAction("slorii X18 X18 12 707")
    tran0.writeAction("slorii X18 X18 12 2236")
    tran0.writeAction("slorii X18 X18 12 1545")
    tran0.writeAction("slorii X18 X18 12 3440")
    tran0.writeAction("sar X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
