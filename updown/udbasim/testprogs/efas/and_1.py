from EFA_v2 import *
def and_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -30760")
    tran0.writeAction("slorii X16 X16 12 2751")
    tran0.writeAction("slorii X16 X16 12 471")
    tran0.writeAction("slorii X16 X16 12 1054")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("movir X17 -24177")
    tran0.writeAction("slorii X17 X17 12 2605")
    tran0.writeAction("slorii X17 X17 12 2208")
    tran0.writeAction("slorii X17 X17 12 1040")
    tran0.writeAction("slorii X17 X17 12 1736")
    tran0.writeAction("movir X18 -32368")
    tran0.writeAction("slorii X18 X18 12 2154")
    tran0.writeAction("slorii X18 X18 12 2281")
    tran0.writeAction("slorii X18 X18 12 4016")
    tran0.writeAction("slorii X18 X18 12 4018")
    tran0.writeAction("and X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
