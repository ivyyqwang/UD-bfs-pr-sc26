from EFA_v2 import *
def sr_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 3853")
    tran0.writeAction("slorii X16 X16 12 4060")
    tran0.writeAction("slorii X16 X16 12 2311")
    tran0.writeAction("slorii X16 X16 12 3383")
    tran0.writeAction("slorii X16 X16 12 3448")
    tran0.writeAction("movir X17 -24365")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("slorii X17 X17 12 3960")
    tran0.writeAction("slorii X17 X17 12 2933")
    tran0.writeAction("slorii X17 X17 12 908")
    tran0.writeAction("movir X18 19184")
    tran0.writeAction("slorii X18 X18 12 820")
    tran0.writeAction("slorii X18 X18 12 3786")
    tran0.writeAction("slorii X18 X18 12 34")
    tran0.writeAction("slorii X18 X18 12 3075")
    tran0.writeAction("sr X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
