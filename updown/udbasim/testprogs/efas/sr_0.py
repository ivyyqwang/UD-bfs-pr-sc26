from EFA_v2 import *
def sr_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 1214")
    tran0.writeAction("slorii X16 X16 12 2652")
    tran0.writeAction("slorii X16 X16 12 632")
    tran0.writeAction("slorii X16 X16 12 622")
    tran0.writeAction("slorii X16 X16 12 3404")
    tran0.writeAction("movir X17 -32768")
    tran0.writeAction("slorii X17 X17 12 2719")
    tran0.writeAction("slorii X17 X17 12 2081")
    tran0.writeAction("slorii X17 X17 12 3542")
    tran0.writeAction("slorii X17 X17 12 3345")
    tran0.writeAction("movir X18 16778")
    tran0.writeAction("slorii X18 X18 12 1679")
    tran0.writeAction("slorii X18 X18 12 2057")
    tran0.writeAction("slorii X18 X18 12 465")
    tran0.writeAction("slorii X18 X18 12 3780")
    tran0.writeAction("sr X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
