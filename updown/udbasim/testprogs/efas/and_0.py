from EFA_v2 import *
def and_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -32511")
    tran0.writeAction("slorii X16 X16 12 3381")
    tran0.writeAction("slorii X16 X16 12 1362")
    tran0.writeAction("slorii X16 X16 12 606")
    tran0.writeAction("slorii X16 X16 12 2527")
    tran0.writeAction("movir X17 -25405")
    tran0.writeAction("slorii X17 X17 12 3277")
    tran0.writeAction("slorii X17 X17 12 3471")
    tran0.writeAction("slorii X17 X17 12 780")
    tran0.writeAction("slorii X17 X17 12 389")
    tran0.writeAction("movir X18 -3116")
    tran0.writeAction("slorii X18 X18 12 436")
    tran0.writeAction("slorii X18 X18 12 3922")
    tran0.writeAction("slorii X18 X18 12 2759")
    tran0.writeAction("slorii X18 X18 12 712")
    tran0.writeAction("and X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
