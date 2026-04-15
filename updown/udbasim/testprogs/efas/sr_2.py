from EFA_v2 import *
def sr_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 25405")
    tran0.writeAction("slorii X16 X16 12 173")
    tran0.writeAction("slorii X16 X16 12 46")
    tran0.writeAction("slorii X16 X16 12 2133")
    tran0.writeAction("slorii X16 X16 12 1589")
    tran0.writeAction("movir X17 -29271")
    tran0.writeAction("slorii X17 X17 12 1214")
    tran0.writeAction("slorii X17 X17 12 891")
    tran0.writeAction("slorii X17 X17 12 274")
    tran0.writeAction("slorii X17 X17 12 3943")
    tran0.writeAction("movir X18 -20867")
    tran0.writeAction("slorii X18 X18 12 454")
    tran0.writeAction("slorii X18 X18 12 726")
    tran0.writeAction("slorii X18 X18 12 3830")
    tran0.writeAction("slorii X18 X18 12 2512")
    tran0.writeAction("sr X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
